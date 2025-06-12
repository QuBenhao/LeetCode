package problems.problems_2616;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private boolean check(int[] nums, int p, int mid) {
        int count = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i + 1] - nums[i] <= mid) {
                count++;
                i++; // Skip the next element as it's already paired
            }
            if (count >= p) {
                return true;
            }
        }
        return false;
    }

    public int minimizeMax(int[] nums, int p) {
        Arrays.sort(nums);
        int left = 0, right = nums[nums.length - 1] - nums[0];
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (check(nums, p, mid)) {
                right = mid; // Try to find a smaller maximum difference
            } else {
                left = mid + 1; // Increase the minimum possible maximum difference
            }
        }
        return left; // The smallest maximum difference that allows at least p pairs
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int p = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minimizeMax(nums, p));
    }
}
