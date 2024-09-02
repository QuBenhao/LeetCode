package problems.problems_2708;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maxStrength(int[] nums) {
        long max = nums[0], min = nums[0];
        for (int i = 1; i < nums.length; i++) {
            long tmp = max, num = nums[i];
            max = Math.max(Math.max(Math.max(max * num, min * num), num), Math.max(max, min));
            min = Math.min(Math.min(Math.min(tmp * num, min * num), num), Math.min(max, min));
        }
        return max;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxStrength(nums));
    }
}
