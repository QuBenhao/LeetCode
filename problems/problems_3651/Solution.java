package problems.problems_3651;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minCost(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        int[][][] dp = new int[k + 1][m][n];
        Map<Integer, List<int[]>> graph = new TreeMap<>();
        for (int i = 0; i <= k; i++) {
            for (int j = 0; j < m; j++) {
                Arrays.fill(dp[i][j], Integer.MAX_VALUE);
            }
        }
        dp[0][0][0] = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                graph.computeIfAbsent(-grid[i][j], x -> new ArrayList<>()).add(new int[]{i, j});
                if (i + 1 < m) {
                    dp[0][i + 1][j] = Math.min(dp[0][i + 1][j], dp[0][i][j] + grid[i + 1][j]);
                }
                if (j + 1 < n) {
                    dp[0][i][j + 1] = Math.min(dp[0][i][j + 1], dp[0][i][j] + grid[i][j + 1]);
                }
            }
        }
        for (int kk = 1; kk <= k; ++kk) {
            int mn = Integer.MAX_VALUE;
            for (List<int[]> list : graph.values()) {
                for (int[] pos : list) {
                    mn = Math.min(mn, dp[kk - 1][pos[0]][pos[1]]);
                }
                for (int[] pos: list) {
                    dp[kk][pos[0]][pos[1]] = mn;
                }
            }
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (i + 1 < m) {
                        dp[kk][i + 1][j] = Math.min(dp[kk][i + 1][j], dp[kk][i][j] + grid[i + 1][j]);
                    }
                    if (j + 1 < n) {
                        dp[kk][i][j + 1] = Math.min(dp[kk][i][j + 1], dp[kk][i][j] + grid[i][j + 1]);
                    }
                }
            }
        }
        int ans = Integer.MAX_VALUE;
        for (int i = 0; i <= k; ++i) {
            ans = Math.min(ans, dp[i][m - 1][n - 1]);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] grid = jsonArrayToInt2DArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minCost(grid, k));
    }
}
