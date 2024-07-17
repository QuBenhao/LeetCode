package problems.problems_198;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int rob(int[] nums) {
        int dp0 = 0, dp1 = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int newDp0 = Math.max(dp0, dp1);
            dp1 = Math.max(dp0 + nums[i], dp1);
            dp0 = newDp0;
        }
        return Math.max(dp0, dp1);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(rob(nums));
    }
}
