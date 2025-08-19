package problems.problems_1277;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countSquares(int[][] matrix) {
        int m = matrix.length, n = matrix[0].length;
        int ans = 0;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == 1) {
                    dp[i + 1][j + 1] = Math.min(dp[i][j], Math.min(dp[i + 1][j], dp[i][j + 1])) + 1;
                    ans += dp[i + 1][j + 1];
                }
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] matrix = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(countSquares(matrix));
    }
}
