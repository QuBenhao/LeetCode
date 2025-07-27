package problems.problems_1260;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<Integer>> shiftGrid(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        k %= m * n;
        if (k == 0) {
            return Arrays.stream(grid)
                    .map(row -> Arrays.stream(row).boxed().toList())
                    .toList();
        }
        int x = k / n, y = k % n;
        int[][] result = new int[m][n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result[x][y] = grid[i][j];
                if (++y == n) {
                    y = 0;
                    ++x;
                }
                x %= m;
            }
        }
        return Arrays.stream(result)
                .map(row -> Arrays.stream(row).boxed().toList())
                .toList();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] grid = jsonArrayToInt2DArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(shiftGrid(grid, k));
    }
}
