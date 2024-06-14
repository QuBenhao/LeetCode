package problems.problems_2786;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maxScore(int[] nums, int x) {
        long ans = nums[0];
        long[] dp = new long[]{Integer.MIN_VALUE, Integer.MIN_VALUE};
        dp[nums[0] % 2] = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int idx = nums[i] % 2;
            long cur = Math.max(dp[idx] + nums[i], dp[idx ^ 1] + nums[i] - x);
            ans = Math.max(ans, cur);
            dp[idx] = Math.max(dp[idx], cur);
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
		int x = Integer.parseInt(values[1]);
        return JSON.toJSON(maxScore(nums, x));
    }
}
