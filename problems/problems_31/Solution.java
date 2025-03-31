package problems.problems_31;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    private void reverse(int[] nums, int start, int end) {
        while (start < end) {
            swap(nums, start, end);
            start++;
            end--;
        }
    }
    public void nextPermutation(int[] nums) {
        int n = nums.length;
        int idx = n - 1;
        while (idx > 0 && nums[idx - 1] >= nums[idx]) {
            idx--;
        }
        if (idx == 0) {
            reverse(nums, 0, n - 1);
            return;
        }
        int i = n - 1;
        while (i >= idx && nums[i] <= nums[idx - 1]) {
            i--;
        }
        swap(nums, idx - 1, i);
        reverse(nums, idx, n - 1);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		nextPermutation(nums);
        return JSON.toJSON(nums);
    }
}
