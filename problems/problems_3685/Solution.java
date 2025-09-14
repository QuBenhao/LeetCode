package problems.problems_3685;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean[] subsequenceSumAfterCapping(int[] nums, int k) {
        int n = nums.length;
        int[] freq = new int[n + 1];
        for (int num: nums) {
            ++freq[num];
        }
        boolean[] ans = new boolean[n];
        boolean[] dp = new boolean[k + 1];
        dp[0] = true;
        int used = 0;
        for (int i = 0; i < n; ++i) {
            int num = i + 1;
            for (int j = 0; j < freq[num]; ++j) {
                for (int x = k; x >= num; --x) {
                    dp[x] = dp[x] || dp[x - num];
                }
            }
            used += freq[num];
            for (int j = 0; j <= Math.min(k / num, n - used); ++j) {
                if (dp[k - j * num]) {
                    ans[i] = true;
                    break;
                }
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(subsequenceSumAfterCapping(nums, k));
    }
}
