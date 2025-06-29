package problems.problems_209;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int left = 0, prefixSum = 0, minLength = Integer.MAX_VALUE;
        for (int right = 0; right < n; right++) {
            prefixSum += nums[right];
            while (prefixSum >= target) {
                minLength = Math.min(minLength, right - left + 1);
                prefixSum -= nums[left++];
            }
        }
        return minLength == Integer.MAX_VALUE ? 0 : minLength;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int target = Integer.parseInt(inputJsonValues[0]);
		int[] nums = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minSubArrayLen(target, nums));
    }
}
