package problems.problems_741;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;

public class Solution extends BaseSolution {
    public int cherryPickup(int[][] grid) {
        int n = grid.length;
        int[][][] dp = new int[n * 2 + 1][n + 1][n + 1];
        for (int[][] layer : dp) {
            for (int[] row : layer) {
                Arrays.fill(row, Integer.MIN_VALUE);
            }
        }
        dp[2][1][1] = grid[0][0];

        for (int step = 3; step <= n * 2; step++) {
            for (int i1 = Math.max(1, step - n); i1 <= Math.min(step - 1, n); i1++) {
                for (int i2 = i1; i2 <= Math.min(step - 1, n); i2++) {
                    int j1 = step - i1, j2 = step - i2;
                    int v1 = grid[i1 - 1][j1 - 1], v2 = grid[i2 - 1][j2 - 1];
                    if (v1 == -1 || v2 == -1) {
                        continue;
                    }
                    dp[step][i1][i2] = i1 == i2 ? v1 : v1 + v2;
                    dp[step][i1][i2] += Math.max(
                            Math.max(dp[step - 1][i1 - 1][i2 - 1],
                                    dp[step - 1][i1 - 1][i2]),
                            Math.max(dp[step - 1][i1][i2 - 1],
                                    dp[step - 1][i1][i2]));
                }
            }
        }

        return Math.max(0, dp[n * 2][n][n]);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] grid = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(cherryPickup(grid));
    }
}
