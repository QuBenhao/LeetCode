package problems.problems_2044;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countMaxOrSubsets(int[] nums) {
        int ans = 0;
        int maxOr = 0;
        int n = nums.length;
        int mask = 1 << n;
        int[] dp = new int[mask];
        for (int i = 1; i < mask; i++) {
            int lowbit = i & -i;
            int prev = i ^ lowbit;
            int idx = 31 - Integer.numberOfLeadingZeros(lowbit);
            dp[i] = dp[prev] | nums[idx];
            if (dp[i] > maxOr) {
                maxOr = dp[i];
                ans = 1;
            } else if (dp[i] == maxOr) {
                ans++;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(countMaxOrSubsets(nums));
    }
}
