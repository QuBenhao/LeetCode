/*
 * @author Jeffrey Chan & Minyi Li, RMIT 2020
 */

package solver;

import java.util.HashSet;

import grid.KillerSudokuGrid;
import grid.KillerSudokuGrid.Cage;
import grid.SudokuGrid;


/**
 * Backtracking solver for Killer Sudoku.
 */
public class KillerBackTrackingSolver extends KillerSudokuSolver
{
	private KillerSudokuGrid grid;
    public KillerBackTrackingSolver() {
    } // end of KillerBackTrackingSolver()


    @Override
    public boolean solve(SudokuGrid grid) {
    	this.grid = (KillerSudokuGrid)grid;
        // placeholder
        return solve(0,0);
    } // end of solve()
    
    private boolean solve(int row, int column) {
    	if (column == grid.getSize())
			return solve(row + 1, 0);
		if (row == grid.getSize())
			return true;
		if (grid.getBoard().get(grid.getPosition(row, column)).getValue()==0) {
			for (int i = 0; i < grid.getBoard().get(grid.getPosition(row, column)).getValues().size(); i++) {
				if (valid(row, column, grid.getBoard().get(grid.getPosition(row, column)).getValues().get(i))) {
					grid.getBoard().get(grid.getPosition(row, column)).setValue(grid.getBoard().get(grid.getPosition(row, column)).getValues().get(i));
					if (solve(row, column + 1)) {
						return true;
					}
					grid.getBoard().get(grid.getPosition(row, column)).setValue(0);
				}
			}
		}
		else
			return solve(row, column + 1);
		return false;
    }
    
    private boolean valid(int row, int column, int value) {
		int size = grid.getSize();
		
		// Row constraint
		for (int c = 0; c < size; c++) {
			if (c == column)
				continue;
			if(grid.getBoard().get(grid.getPosition(row, c)).getValue()==value)
				return false;
		}

		// Column constraint
		for (int r = 0; r < size; r++) {
			if (r == row)
				continue;
			if(grid.getBoard().get(grid.getPosition(r, column)).getValue()==value)
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
				if(grid.getBoard().get(grid.getPosition(r, c)).getValue()==value)
					return false;
			}
		}

		// Cage constraint
		for(Cage cage:grid.getCages()) {
			if(cage.getCells().contains(this.grid.new Cell(row,column))) {
					HashSet<Integer> set = new HashSet<>();
					int sum = 0;
					boolean checkSum = true;
					for(int i=0;i<cage.getCells().size();i++) {
						int r = cage.getCells().get(i).getRow();
						int c = cage.getCells().get(i).getColumn();
						if(r == row && c == column) {
							continue;
						}
						if(grid.getBoard().get(grid.getPosition(r, c)).getValue()!=0) {
							set.add(grid.getBoard().get(grid.getPosition(r, c)).getValue());
							sum += grid.getBoard().get(grid.getPosition(r, c)).getValue();
						}
						else
							checkSum = false;
					}
					
					if(set.contains(value))
						return false;
					if(checkSum) {
						if(value + sum != cage.getSum())
							return false;
					}
					else if(value > cage.getSum())
						return false;
					break;
			}
		}
		
		return true;
	}

} // end of class KillerBackTrackingSolver()
