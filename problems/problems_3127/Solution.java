package problems.problems_3127;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canMakeSquare(char[][] grid) {
        int m = grid.length, n = grid[0].length;
        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n - 1; j++) {
                int count = 0;
                for (int r = i; r < i + 2; r++) {
                    for (int c = j; c < j + 2; c++) {
                        if (grid[r][c] == 'B') {
                            count++;
                        }
                    }
                }
                if (count != 2) {
                    return true;
                }
            }
        }
        return false;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[][] grid = jsonArrayToChar2DArray(inputJsonValues[0]);
        return JSON.toJSON(canMakeSquare(grid));
    }
}
