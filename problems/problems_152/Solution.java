package problems.problems_152;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxProduct(int[] nums) {
        int ans = nums[0], dp_max = nums[0], dp_min = nums[0];
        for (int i = 1; i < nums.length; i++) {
            int temp = dp_max;
            dp_max = Math.max(Math.max(dp_max * nums[i], dp_min * nums[i]), nums[i]);
            dp_min = Math.min(Math.min(temp * nums[i], dp_min * nums[i]), nums[i]);
            ans = Math.max(ans, dp_max);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxProduct(nums));
    }
}
