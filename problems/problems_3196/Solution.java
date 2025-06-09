package problems.problems_3196;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maximumTotalCost(int[] nums) {
        int n = nums.length;
        long f0 = nums[0], f1 = nums[0];
        for (int i = 1; i < n; ++i) {
            long tmp = f1 - nums[i];
            f1 = Math.max(f0, f1) + nums[i];
            f0 = tmp;
        }
        return Math.max(f0, f1);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maximumTotalCost(nums));
    }
}
