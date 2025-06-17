package problems.problems_808;

import java.util.Arrays;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double soupServings(int n) {
        if (n == 0) {
            return 0.5;
        }
        n = (n + 24) / 25; // Convert to servings of 25 ml
        if (n >= 178) {
            return 1.0; // If n is large enough, return 1.0
        }
        double[][] dp = new double[n + 1][n + 1];
        Arrays.fill(dp[0], 1.0); // If soup A is empty, soup B will finish
        dp[0][0] = 0.5; // Base case: both soups empty
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                dp[i][j] = 0.25 * (dp[Math.max(i - 4, 0)][j] + dp[Math.max(i - 3, 0)][Math.max(j - 1, 0)] +
                                  dp[Math.max(i - 2, 0)][Math.max(j - 2, 0)] + dp[Math.max(i-1, 0)][Math.max(j - 3, 0)]);
            }
        }
        return dp[n][n];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(soupServings(n));
    }
}
