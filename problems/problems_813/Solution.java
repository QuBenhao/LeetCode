package problems.problems_813;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double largestSumOfAverages(int[] nums, int k) {
        int n = nums.length;
        int[] prefixSum = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
        double[][] dp = new double[n + 1][k + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= Math.min(i, k); j++) {
                if (j == 1) {
                    dp[i][j] = Math.max(dp[i][j], (double) (prefixSum[i] - prefixSum[0]) / i);
                } else {
                    for (int l = j-1; l < i; l++) {
                        dp[i][j] = Math.max(dp[i][j], dp[l][j - 1] + (double) (prefixSum[i] - prefixSum[l]) / (i - l));
                    }
                }
            }
        }
        return dp[n][k];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(largestSumOfAverages(nums, k));
    }
}
