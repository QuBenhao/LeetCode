package problems.problems_3603;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minCost(int m, int n, int[][] waitCost) {
        long[][] dp = new long[m][n];
        for (int i = 0; i < m; ++i) {
            Arrays.fill(dp[i], Long.MAX_VALUE);
        }
        dp[0][0] = 1;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i < m - 1) {
                    dp[i + 1][j] = Math.min(dp[i + 1][j], dp[i][j] + waitCost[i + 1][j] + (2L + i) * (1L + j));
                }
                if (j < n - 1) {
                    dp[i][j + 1] = Math.min(dp[i][j + 1], dp[i][j] + waitCost[i][j + 1] + (1L + i) * (2L + j));
                }
            }
        }
        return dp[m - 1][n - 1] - waitCost[m - 1][n - 1];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int m = Integer.parseInt(inputJsonValues[0]);
		int n = Integer.parseInt(inputJsonValues[1]);
		int[][] waitCost = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(minCost(m, n, waitCost));
    }
}
