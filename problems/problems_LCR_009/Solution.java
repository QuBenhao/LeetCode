package problems.problems_LCR_009;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        int ans = 0;
        int cur = 1;
        for (int left = 0, right = 0; right < nums.length; right++) {
            cur *= nums[right];
            while (left <= right && cur >= k) {
                cur /= nums[left];
                left++;
            }
            ans += right - left + 1;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(numSubarrayProductLessThanK(nums, k));
    }
}
