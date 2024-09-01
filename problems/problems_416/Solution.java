package problems.problems_416;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canPartition(int[] nums) {
        int s = 0;
        for (int num : nums) {
            s += num;
        }
        if (s % 2 == 1) {
            return false;
        }
        int target = s / 2;
        boolean[] dp = new boolean[target + 1];
        dp[0] = true;
        for (int num : nums) {
            for (int i = target; i >= num; i--) {
                dp[i] = dp[i] || dp[i - num];
            }
        }
        return dp[target];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(canPartition(nums));
    }
}
