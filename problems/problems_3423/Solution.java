package problems.problems_3423;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxAdjacentDistance(int[] nums) {
        int ans = Math.abs(nums[0] - nums[nums.length-1]);
        for (int i = 0; i < nums.length - 1; i++) {
            ans = Math.max(ans, Math.abs(nums[i] - nums[i + 1]));
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxAdjacentDistance(nums));
    }
}
