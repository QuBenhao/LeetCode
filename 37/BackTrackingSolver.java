/*
 * @author Jeffrey Chan & Minyi Li, RMIT 2020
 */

package solver;

import grid.StdSudokuGrid;
import grid.SudokuGrid;

/**
 * Backtracking solver for standard Sudoku.
 */
public class BackTrackingSolver extends StdSudokuSolver {

	public BackTrackingSolver() {
	} // end of BackTrackingSolver()

	@Override
	public boolean solve(SudokuGrid grid) {
		if (grid instanceof StdSudokuGrid)
			return solve((StdSudokuGrid) grid, 0, 0);
		else
			return false;
	} // end of solve()

	private boolean solve(StdSudokuGrid grid, int row, int column) {
		if (column == grid.getSize())
			return solve(grid, row + 1, 0);
		if (row == grid.getSize())
			return true;
		if (!grid.getBoard().containsKey(grid.getPosition(row, column)))
			for (int i = 0; i < grid.getSize(); i++) {
				if (valid(grid, row, column, grid.getValues()[i])) {
					grid.getBoard().put(grid.getPosition(row, column), grid.getValues()[i]);
					if (solve(grid, row, column + 1))
						return true;
					else
						grid.getBoard().remove(grid.getPosition(row, column));
				}
			}
		else
			return solve(grid, row, column + 1);
		return false;
	}

	private boolean valid(StdSudokuGrid grid, int row, int column, int value) {
		int size = grid.getSize();
		
		// Row constraint
		for (int c = 0; c < size; c++) {
			if (c == column)
				continue;
			if(grid.getBoard().containsKey(grid.getPosition(row, c)))
				if (grid.getBoard().get(grid.getPosition(row, c)) == value)
					return false;
		}

		// Column constraint
		for (int r = 0; r < size; r++) {
			if (r == row)
				continue;
			if(grid.getBoard().containsKey(grid.getPosition(r, column)))
				if (grid.getBoard().get(grid.getPosition(r, column)) == value)
					return false;
		}

		// Box constraint
		int box = (int) Math.pow(size, 0.5);
		int rbox = row / box;
		int cbox = column / box;
		for (int r = rbox * box; r < (rbox + 1) * box; r++) {
			for (int c = cbox * box; c < (cbox + 1) * box; c++) {
				if (r == row && c == column)
					continue;
				if(grid.getBoard().containsKey(grid.getPosition(r, c)))
					if (grid.getBoard().get(grid.getPosition(r, c)) == value)
						return false;
			}
		}

		return true;
	}
} // end of class BackTrackingSolver()
