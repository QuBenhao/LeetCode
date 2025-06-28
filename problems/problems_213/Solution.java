package problems.problems_213;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;

public class Solution extends BaseSolution {
    private int robHelper(int[] nums, int start, int end) {
        int rob = nums[start], notRob = 0;
        for (int i = start + 1; i <= end; i++) {
            int newRob = notRob + nums[i];
            notRob = Math.max(rob, notRob);
            rob = newRob;
        }
        return Math.max(rob, notRob);
    }

    public int rob(int[] nums) {
        int n = nums.length;
        if (n == 1)
            return nums[0];
        return Math.max(robHelper(nums, 0, n - 2), robHelper(nums, 1, n - 1));
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(rob(nums));
    }
}
