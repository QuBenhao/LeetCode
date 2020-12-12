/*
 * @author Jeffrey Chan & Minyi Li, RMIT 2020
 */
package solver;

import grid.SudokuGrid;

import java.util.ArrayList;

import grid.StdSudokuGrid;

/**
 * Algorithm X solver for standard Sudoku.
 */
public class AlgorXSolver extends StdSudokuSolver {

	private final static int CONSTRAINTS = 4;
	private int size;
	private StdSudokuGrid grid;
	boolean[][] coverBoard;
	ArrayList<Integer> solution = new ArrayList<>();
	ArrayList<Integer> head = new ArrayList<>();
	
	public AlgorXSolver() {
	} // end of AlgorXSolver()

	@Override
	public boolean solve(SudokuGrid grid) {
		assert (grid instanceof StdSudokuGrid);
		this.grid = (StdSudokuGrid) grid;
		size = this.grid.getSize();
		coverBoard = new boolean[(int)Math.pow(size, 3)][(int)Math.pow(size, 2)*CONSTRAINTS];
		for(int i = 0; i<(int)Math.pow(size, 2)*CONSTRAINTS;i++) {
			head.add(i);
			for(int j=0;j<size;j++) {
				coverBoard[rowRange(i)[j]][i] = true;
			}
		}
		for(int r=0;r<size;r++) {
			for(int c=0;c<size;c++) {
				if(this.grid.getBoard().containsKey(this.grid.getPosition(r, c))) {
					int value = this.grid.getBoard().get(this.grid.getPosition(r, c));
					for(int j=0;j<size;j++) {
						if(this.grid.getValues()[j] == value) {
							int rIndex = r * (int)Math.pow(size,2) + c * size + j;
							for(int k =0;k<CONSTRAINTS;k++) {
								head.remove((Integer)columnRange(rIndex)[k]);
							}
							remove(rIndex);
							break;
						}
					}
				}
			}
		}
		return solve();
	} // end of solve()

	/*
	 * 1. If the matrix A has no columns, the current partial solution is a valid solution; terminate successfully. 
	 * 2. Otherwise, choose a column c (deterministically). 
	 * 3. Choose a row r such that A[r] = 1 (nondeterministically). 
	 * 4. Include row r in the partial solution. 
	 * 5. For each column j such that A[r][j] = 1, 
	 * 		for each row i such that A[i][j] = 1, 
	 * 			delete row i from matrix A. 
	 * 		delete column j from matrix A. 
	 * 6. Repeat this algorithm recursively on the reduced matrix A.
	 */
	
	private boolean solve(){
		int cIndex = minColumn();
		if(cIndex == -1) {
			if(!head.isEmpty())
				return false;
			// 1. If the matrix A has no columns, the current partial solution is a valid solution; terminate successfully. 
			for(Integer rIndex: solution) {
				int row = rIndex / (int) Math.pow(size, 2);
				int column = rIndex % (int) Math.pow(size, 2) / size;
				int valueIndex = (rIndex % (int) Math.pow(size, 2))% size;
				this.grid.getBoard().put(this.grid.getPosition(row, column), this.grid.getValues()[valueIndex]);
			}
			return true;
		}
		for(int i=0;i<size;i++) {
			// 3. Choose a row r such that A[r] = 1 (nondeterministically). 
			int rIndex = rowRange(cIndex)[i];
			if(coverBoard[rIndex][cIndex]) {
				// 4. Include row r in the partial solution. 
				solution.add(rIndex);
				for(int k =0;k<CONSTRAINTS;k++) {
					head.remove((Integer)columnRange(rIndex)[k]);
				}
				ArrayList<Operation> operations;
				operations = remove(rIndex);
				// 6. Repeat this algorithm recursively on the reduced matrix A.
				if(solve()) {
					return true;
				}
				solution.remove((Integer)rIndex);
				for(int k =0;k<CONSTRAINTS;k++) {
					head.add((Integer)columnRange(rIndex)[k]);
				}
				for(Operation o:operations) {
					coverBoard[o.row][o.column] = true;
				}
			}
		}
		return false;
	}
	
	/* 5. For each column j such that A[r][j] = 1,
	 * 		for each row i such that A[i][j] = 1, 
	 * 			delete row i from matrix A. 
	 * 		delete column j from matrix A. 
	*/
	
	private ArrayList<Operation> remove(int rIndex) {
		ArrayList<Operation> operations = new ArrayList<>();
		for(int i=0;i<CONSTRAINTS;i++) {
			int cIndex = columnRange(rIndex)[i];
			for(int j=0;j<size;j++) {
				if(coverBoard[rowRange(cIndex)[j]][cIndex]) {
					for(int k=0;k<CONSTRAINTS;k++) {
						coverBoard[rowRange(cIndex)[j]][columnRange(rowRange(cIndex)[j])[k]] = false;
						operations.add(new Operation(rowRange(cIndex)[j],columnRange(rowRange(cIndex)[j])[k]));
					}
				}
			}
		}
		return operations;
	}

	//  2. Otherwise, choose a column c (deterministically). 
	private int minColumn() {
		int index = -1;
		int count;
		int min = size + 1;
		for(Integer i: head) {
			count = 0;
			for(int j=0;j<size;j++) {
				if(coverBoard[rowRange(i)[j]][i])
					count++;
			}
			if(count == 0) {
				index = -1;
				break;
			}
			if(count == 1) {
				index = i;
				break;
			}
			if(count < min) {
				index = i;
				min = count;
			}
		}
		return index;
	}
	
	/*
	 * rowIndex = row * (int)Math.pow(size,2) + column * size + valueIndex; 
	 * columnIndex1 = row * size + column; 
	 * columnIndex2 = (int)Math.pow(size,2) + row * size + valueIndex; 
	 * columnIndex3 = (int)Math.pow(size,2) * 2 + column * size + valueIndex;
	 * columnIndex4 = (int)Math.pow(size,2) * 3 + (row/(int)Math.pow(size,0.5) * (int)Math.pow(size,0.5) + c / (int)Math.pow(size,0.5)) * size + valueIndex;
	 */
	
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
	
	private class Operation{
		private int row;
		private int column;
		public Operation(int row,int column) {
			this.row = row;
			this.column = column;
		}
	}
} // end of class AlgorXSolver
