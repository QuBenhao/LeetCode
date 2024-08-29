package problems.problems_3142;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean satisfiesConditions(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        for (int j = 0; j < n - 1; j++) {
            if (grid[0][j] == grid[0][j + 1]) {
                return false;
            }
        }
        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] != grid[i + 1][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] grid = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(satisfiesConditions(grid));
    }
}
