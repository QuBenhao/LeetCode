package problems.problems_494;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findTargetSumWays(int[] nums, int target) {
        int t = target;
        for (int num: nums) {
            target += num;
        }
        if (target % 2 != 0 || target < 0 || target < 2 * t) {
            return 0;
        }
        target >>= 1;
        int[] dp = new int[target + 1];
        dp[0] = 1;
        for (int num: nums) {
            for (int x = target; x >= num; x--) {
                dp[x] += dp[x - num];
            }
        }
        return dp[target];
    }



    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
		int target = Integer.parseInt(values[1]);
        return JSON.toJSON(findTargetSumWays(nums, target));
    }
}
