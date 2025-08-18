package problems.problems_2348;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long zeroFilledSubarray(int[] nums) {
        int n = nums.length;
        long ans = 0;
        int left = 0;
        for (int right = 0; right < n; ++right) {
            while (left < n && nums[left] != 0) {
                ++left;
            }
            right = left;
            while (right < n && nums[right] == 0) {
                ++right;
            }
            ans += 1L * (right - left) * (1L + right - left) / 2L;
            left = right;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(zeroFilledSubarray(nums));
    }
}
