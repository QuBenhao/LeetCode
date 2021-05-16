/*
 * @author Jeffrey Chan & Minyi Li, RMIT 2020
 */

package solver;

import java.util.ArrayList;
import java.util.HashMap;

import grid.StdSudokuGrid;
import grid.SudokuGrid;


/**
 * Dancing links solver for standard Sudoku.
 */
public class DancingLinksSolver extends StdSudokuSolver
{
	private ColumnNode h;
	private StdSudokuGrid grid;
	private int size;
	private static final int CONSTRAINTS = 4;
	private ArrayList<DancingNode> solution;
	private HashMap<Integer,ColumnNode> headerList;

	public DancingLinksSolver() {
		h = new ColumnNode();
		solution = new ArrayList<>();
		headerList = new HashMap<>();
	} // end of DancingLinksSolver()

	@Override
	public boolean solve(SudokuGrid grid) {
		assert (grid instanceof StdSudokuGrid);
		this.grid = (StdSudokuGrid) grid;
		size = this.grid.getSize();
		for (int i = 0; i < (int) Math.pow(size, 2) * CONSTRAINTS; i++) {
			ColumnNode c = new ColumnNode(i);
			headerList.put(i, c);
			for (int j = 0; j < size; j++) {
				DancingNode node = new DancingNode(c);
				c.linkDown(node);
				if(j==0) {
					node.D = c;
					c.U = node;
				}
			}
			if(i==0)
				h.linkRight(c);
			else
				headerList.get(i-1).linkRight(c);
			if(i == (int) Math.pow(size, 2) * CONSTRAINTS-1) {
				c.R = h;
				h.L = c;
			}
		}
		for(int i=0;i<(int)Math.pow(size, 2);i++) {
			for(int j=0;j<size;j++){
				int rIndex = rowRange(i)[j];
				DancingNode r = findNode(headerList.get(columnRange(rIndex)[0]),rIndex,columnRange(rIndex)[0]);
				for(int k=CONSTRAINTS-1;k>0;k--) {
					DancingNode c = findNode(headerList.get(columnRange(rIndex)[k]),rIndex,columnRange(rIndex)[k]);
					r.linkRight(c);
					if(k==CONSTRAINTS-1) {
						r.L = c;
						c.R = r;
					}
				}
			}
		}
		
		for(int r=0;r<size;r++) {
			for(int c=0;c<size;c++) {
				if(this.grid.getBoard().containsKey(this.grid.getPosition(r, c))) {
					int value = this.grid.getBoard().get(this.grid.getPosition(r, c));
					int j;
					for(j=0;j<size;j++) {
						if(this.grid.getValues()[j] == value)
							break;
					}
					int rIndex = r * (int)Math.pow(size,2) + c * size + j;
					for(int k=0;k<CONSTRAINTS;k++){
						cover(headerList.get(columnRange(rIndex)[k]));
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
				grid.getBoard().put(grid.getPosition(row, column), grid.getValues()[valueIndex]);
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
	 * rowIndex = row * (int)Math.pow(size,2) + column * size + valueIndex; 
	 * columnIndex1 = row * size + column; 
	 * columnIndex2 = (int)Math.pow(size,2) + row * size + valueIndex; 
	 * columnIndex3 = (int)Math.pow(size,2) * 2 + column * size + valueIndex;
	 * columnIndex4 = (int)Math.pow(size,2) * 3 + (row/(int)Math.pow(size,0.5) * (int)Math.pow(size,0.5) + c / (int)Math.pow(size,0.5)) * size + valueIndex;
	 */
	private DancingNode findNode(ColumnNode c,int rIndex,int cIndex) {
		DancingNode node = c.D;
		for(int i=0;i<size;i++) {
			if(rowRange(cIndex)[i]==rIndex) {
				break;
			}
			node = node.D;
		}
		return node;
	}
	
	public int[] rowRange(int cIndex) {
		int[] rows = new int[size];
		int row;
		int column;
		int valueIndex;
		switch (cIndex / (int) Math.pow(size, 2)) {
		case 0:
			column = cIndex % size;
			row = cIndex / size;
			for (int i = 0; i < size; i++) {
				rows[i] = row * (int) Math.pow(size, 2) + column * size + i;
			}
			break;
		case 1:
			cIndex = cIndex - (int) Math.pow(size, 2);
			row = cIndex / size;
			valueIndex = cIndex % size;
			for (int c = 0; c < size; c++) {
				rows[c] = row * (int) Math.pow(size, 2) + c * size + valueIndex;
			}
			break;
		case 2:
			cIndex = cIndex - (int) Math.pow(size, 2) * 2;
			column = cIndex / size;
			valueIndex = cIndex % size;
			for (int r = 0; r < size; r++) {
				rows[r] = r * (int) Math.pow(size, 2) + column * size + valueIndex;
			}
			break;
		case 3:
			cIndex = cIndex - (int) Math.pow(size, 2) * 3;
			valueIndex = cIndex % size;
			int box = cIndex / size;
			int boxsize = (int) Math.pow(size, 0.5);
			for (int r = box / boxsize * boxsize; r < (box / boxsize + 1) * boxsize; r++) {
				for (int c = box % boxsize * boxsize; c < (box % boxsize + 1) * boxsize; c++) {
					rows[(r - box / boxsize * boxsize) * boxsize
							+ (c - box % boxsize * boxsize)] = r * (int) Math.pow(size, 2) + c * size + valueIndex;
				}
			}
			break;
		}
		return rows;
	}
	
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

} // end of class DancingLinksSolver
