package problems.problems_2970;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int incremovableSubarrayCount(int[] nums) {
        int n = nums.length;
        int i = 0;
        while (i < n - 1 && nums[i] < nums[i + 1]) {
            i++;
        }
        if (i == n - 1) { // Every nonempty subarray can be removed
            return n * (n + 1) / 2;
        }

        int ans = i + 2; // Cases with no retained suffix: i+2 in total
        // Enumerate nums[j:] as the retained suffix
        for (int j = n - 1; j == n - 1 || nums[j] < nums[j + 1]; j--) {
            while (i >= 0 && nums[i] >= nums[j]) {
                i--;
            }
            // Retain any prefix nums[:i+1], nums[:i], ..., nums[:0]: i+2 choices in total
            ans += i + 2;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(incremovableSubarrayCount(nums));
    }
}
