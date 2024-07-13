package problems.problems_3011;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canSortArray(int[] nums) {
        for (int i = 0, preMax = 0, n = nums.length; i < n; ) {
            int ones = Integer.bitCount(nums[i]), curMax = nums[i];
            for (; i < n && Integer.bitCount(nums[i]) == ones; i++) {
                if (nums[i] < preMax) return false;
                curMax = Math.max(curMax, nums[i]);
            }
            preMax = curMax;
        }
        return true;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(canSortArray(nums));
    }
}
