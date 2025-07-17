package problems.problems_3202;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumLength(int[] nums, int k) {
        int ans = 0;
        for (int val = 0; val < k; val++) {
            int[] dp = new int[k];
            for (int num : nums) {
                num %= k;
                dp[num] = dp[(k + val - num) % k] + 1;
                ans = Math.max(ans, dp[num]);
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maximumLength(nums, k));
    }
}
