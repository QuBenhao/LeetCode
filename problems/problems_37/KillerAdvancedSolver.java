/*
 * @author Jeffrey Chan & Minyi Li, RMIT 2020
 */

package solver;

import java.util.ArrayList;
import java.util.HashMap;

import grid.KillerSudokuGrid;
import grid.StdSudokuGrid;
import grid.KillerSudokuGrid.Cell;
import grid.SudokuGrid;


/**
 * Your advanced solver for Killer Sudoku.
 */
public class KillerAdvancedSolver extends KillerSudokuSolver
{
	private ColumnNode h;
	private KillerSudokuGrid grid;
	private int size;
	private static final int CONSTRAINTS = 4;
	private ArrayList<DancingNode> solution;
	private HashMap<Integer,ColumnNode> headerList;
	
    public KillerAdvancedSolver() {
		h = new ColumnNode();
		solution = new ArrayList<>();
		headerList = new HashMap<>();
    } // end of KillerAdvancedSolver()


    @Override
    public boolean solve(SudokuGrid grid) {
    	assert (grid instanceof StdSudokuGrid);
		this.grid = (KillerSudokuGrid) grid;
		size = this.grid.getSize();
		
		// Column linked-list construct
		for(int i=0;i<(int)Math.pow(size, 2)*CONSTRAINTS + this.grid.sum * size;i++) {
			ColumnNode c = new ColumnNode(i);
			headerList.put(i, c);
			if(i==0)
				h.linkRight(c);
			else
				headerList.get(i-1).linkRight(c);
			if(i == (int) Math.pow(size, 2) * CONSTRAINTS + this.grid.sum * size -1) {
				c.R = h;
				h.L = c;
			}
		}
		
		// Start constructing dancing link by each Cell
		for(int row=0;row<size;row++) {
			for(int column=0;column<size;column++) {
				Cell cell = this.grid.getBoard().get(this.grid.getPosition(row, column));
				int rows = cell.getDancingLinkCells().size();
				ColumnNode c = headerList.get(row*size+column);
				// Each value with specific startPoint
				for(int i=0;i<rows;i++) {
					DancingNode node = new DancingNode(c);
					c.linkDown(node);
					if(i==0) {
						node.D = c;
						c.U = node;
					}
					int valueIndex = getValueIndex(cell.getDancingLinkCells().get(i).getValue());
					int rIndex = row * (int)Math.pow(size,2) + column * size + valueIndex; 
					for(int j=CONSTRAINTS-1;j>0;j--) {
						ColumnNode c1 = headerList.get(columnRange(rIndex)[j]);
						DancingNode constraintsNode = new DancingNode(c1);
						c1.linkDown(constraintsNode);
						node.linkRight(constraintsNode);
						if(j==CONSTRAINTS-1) {
							for(int k=0;k<cell.getDancingLinkCells().get(i).getValue();k++) {
								ColumnNode c2 = headerList.get(getColumnIndex(cell) + cell.getDancingLinkCells().get(i).getStartPoint() + cell.getDancingLinkCells().get(i).getValue()-1-k);
								DancingNode cageNode = new DancingNode(c2);
								c2.linkDown(cageNode);
								constraintsNode.linkRight(cageNode);
								if(k==0) {
									cageNode.R = node;
									node.L = cageNode;
								}
							}
						}
					}
				}
			}
		}
		
        return solve();
    } // end of solve()
    
    /*
     * 	Solve(nondeterministic)
     * 	k = 0.
     *  If R[h] = h, print the current solution and return. 
     *  Otherwise choose a column object c.
     *  Cover column c.
     *  For each r ← D[c], D􏰀D[c]􏰁, ..., while r != c,
     *  	set O[k] ← r;
     *  	for each j ← R[r], R􏰀R[r]􏰁, ..., while j != r,
     *  		cover column j; 
     *  	search(k + 1);
     *  	set r←O[k] and c←C[r];
     *  	for each j ← L[r], L􏰀L[r]􏰁, ..., while j != r,
     *  		uncover column j. 
     *  Uncover column c and return.
     */
    
    /*
     * 	Solve(deterministic)
     *  If R[h] = h, print the current solution and return. 
     *  Otherwise choose a column object c with minimum size.
     *  Cover column c.
     *  For each r ← D[c], D􏰀[D[c]]􏰁, ..., while r != c,
     *  	set O[k] ← r;
     *  	for each j ← R[r], R􏰀[R[r]􏰁], ..., while j != r,
     *  		cover column j; 
     *  	search();
     *  	set r←O[k] and c←C[r];
     *  	for each j ← L[r], L􏰀[L[r]]􏰁, ..., while j != r,
     *  		uncover column j. 
     *  Uncover column c and return.
     */
    
    private boolean solve() {
		if (h.R == h) {
			for (DancingNode i : solution) {
				while (i.c.N >= (int)Math.pow(size, 2))
					i = i.L;
    			/*
    			 * columnIndex1 = row * size + column; 
    			 * columnIndex2 = (int)Math.pow(size,2) + row * size + valueIndex;
    			 */
				int row, column, valueIndex;
				row = i.c.N / size;
				column = i.c.N % size;
				valueIndex = i.R.c.N - (int) Math.pow(size, 2) - row * size;
				grid.getBoard().get((grid.getPosition(row, column))).setValue(grid.getValues()[valueIndex]);
			}
			return true;
		}
		ColumnNode c = findMinColumn();
		if(c==h)
			return false;
		DancingNode r = c.D, j;
		cover(c);
		while (r != c) {
			solution.add(r);
			j = r.R;
			while (j != r) {
				cover(j.c);
				j = j.R;
			}
			if (solve())
				return true;
			solution.remove(r);
			j = r.L;
			while (j != r) {
				uncover(j.c);
				j = j.L;
			}
			r = r.D;
		}
		uncover(c);
		return false;
	}

	private ColumnNode findMinColumn() {
		ColumnNode t = (ColumnNode) h.R;
		ColumnNode min = h;
		int m = size + 1;
		while (t != h) {
			if(t.S == 0 ) {
				min = h;
				break;
			}
			if (t.S < m) {
				m = t.S;
				min = t;
			}
			t = (ColumnNode) t.R;
		}
		return min;
	}
	

    /*
     * 	Cover
     *  Set L[􏰀R[c]􏰁] ← L[c] and R􏰀[L[c]]􏰁 ← R[c].
     *  For each i ← D[c], D􏰀[D[c]]􏰁, ..., while i != c,
     *  	for each j ← R[i], R􏰀[R[i]]􏰁, ..., while j != i, 
     *  		set U􏰀[D[j]􏰁] ← U[j], D[􏰀U[j]]􏰁 ← D[j],
     *  		and set S􏰀[C[j]]􏰁 ← S[􏰀C[j]]􏰁 − 1.
     */
	private void cover(ColumnNode c) {
		c.removeH();
		DancingNode i = c.D;
		DancingNode j;
		while (i != c) {
			j = i.R;
			while (j != i) {
				j.removeV();
				j = j.R;
			}
			i = i.D;
		}
	}
    
    /*
     * 	Uncover
     * 	For each i = U[c], U􏰀[U[c]]􏰁, ..., while i != c,
     * 		for each j ← L[i], L[􏰀L[i]]􏰁, ..., while j != i,
     * 			set S􏰀[C[j]]􏰁 ← S􏰀[j]􏰁 + 1,
     * 			and set U􏰀[D[j]]􏰁 ← j, D[􏰀U[j]]􏰁 ← j. 
     * 	Set L􏰀[R[c]]􏰁 ← c and R􏰀[L[c]]􏰁 ← c.
     */
	private void uncover(ColumnNode c) {
		DancingNode i = c.U;
		DancingNode j;
		while (i != c) {
			j = i.L;
			while (j != i) {
				j.addV();
				j = j.L;
			}
			i = i.U;
		}
		c.addH();
	}
    
    /*
     * Cell, Row, Column, Box constraints
	 * rowIndex = row * (int)Math.pow(size,2) + column * size + valueIndex; 
	 * columnIndex1 = row * size + column; 
	 * columnIndex2 = (int)Math.pow(size,2) + row * size + valueIndex; 
	 * columnIndex3 = (int)Math.pow(size,2) * 2 + column * size + valueIndex;
	 * columnIndex4 = (int)Math.pow(size,2) * 3 + (row/(int)Math.pow(size,0.5) * (int)Math.pow(size,0.5) + c / (int)Math.pow(size,0.5)) * size + valueIndex;
	 */
	public int[] columnRange(int rIndex) {
		int[] columns = new int[CONSTRAINTS];
		int row = rIndex / (int) Math.pow(size, 2);
		int column = rIndex % (int) Math.pow(size, 2) / size;
		int valueIndex = (rIndex % (int) Math.pow(size, 2))% size;
		columns[0] = row * size + column;
		columns[1] = (int) Math.pow(size, 2) + row * size + valueIndex;
		columns[2] = (int) Math.pow(size, 2) * 2 + column * size + valueIndex;
		columns[3] = (int) Math.pow(size, 2) * 3
				+ (row / (int) Math.pow(size, 0.5) * (int) Math.pow(size, 0.5) + column / (int) Math.pow(size, 0.5))
						* size
				+ valueIndex;
		return columns;
	}
	
	private int getValueIndex(int value) {
		for(int i=0;i<grid.getValues().length;i++) {
			if(grid.getValues()[i]==value)
				return i;
		}
		return -1;
	}
	
	// ColumnIndex(StartPoint) for Cell
	private int getColumnIndex(Cell cell) {
		int columnIndex = (int)Math.pow(size, 2) * CONSTRAINTS;
		for(int i=0;i<grid.getCages().size();i++) {
			if(grid.getCages().get(i).getCells().contains(cell))
				break;
			columnIndex += grid.getCages().get(i).getSum();
		}
		return columnIndex;
	}
	
	private class DancingNode {
		DancingNode U, D, L, R;
		ColumnNode c;

		public DancingNode() {
			U = D = L = R = this;
		}

		public DancingNode(ColumnNode c) {
			this();
			this.c = c;
		}

		public void linkRight(DancingNode node) {
				node.L = this;
				node.R = R;
				R.L = node;
				R = node;
		}
		
		public void linkDown(DancingNode node) {
			node.U = this;
			D.U = node;
			node.D = D;
			D = node;
			c.S++;
		}

		public void removeH() {
			L.R = R;
			R.L = L;
		}

		public void removeV() {
			U.D = D;
			D.U = U;
			c.S--;
		}

		public void addH() {
			L.R = this;
			R.L = this;
		}

		public void addV() {
			U.D = this;
			D.U = this;
			c.S++;
		}

	}

	private class ColumnNode extends DancingNode {
		// size
		int S = 0;
		// name
		int N;

		public ColumnNode() {
			super();
			super.c = this;
		}

		public ColumnNode(int N) {
			this();
			this.N = N;
		}
	}
} // end of class KillerAdvancedSolver
