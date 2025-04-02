package problems.problems_2874;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maximumTripletValue(int[] nums) {
        long ans = 0;
        int n = nums.length;
        long[] sufMax = new long[n];
        sufMax[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            sufMax[i] = Math.max(sufMax[i + 1], nums[i]);
        }
        long preMax = nums[0];
        for (int j = 1; j < n - 1; j++) {
            ans = Math.max(ans,  (preMax - nums[j]) * sufMax[j + 1]);
            preMax = Math.max(preMax, nums[j]);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maximumTripletValue(nums));
    }
}
