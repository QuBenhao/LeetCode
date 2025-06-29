package problems.problems_3599;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minXor(int[] nums, int k) {
        int n = nums.length;
        int[] prefixXor = new int[n + 1];
        for (int i = 0; i < n; ++i) {
            prefixXor[i + 1] = prefixXor[i] ^ nums[i];
        }
        int[][] dp = new int[n + 1][k + 1];
        for (int i = 1; i <= n; ++i) {
            Arrays.fill(dp[i], Integer.MAX_VALUE);
            dp[i][1] = prefixXor[i];
        }
        for (int j = 2; j <= k; ++j) {
            for (int i = j; i <= n; ++i) {
                for (int p = j - 1; p < i; ++p) {
                    dp[i][j] = Math.min(dp[i][j], Math.max(dp[p][j - 1], prefixXor[i] ^ prefixXor[p]));
                }
            }
        }
        return dp[n][k];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minXor(nums, k));
    }
}
