package problems.problems_775;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isIdealPermutation(int[] nums) {
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            // Check if the absolute difference between the current index and the value at that index is greater than 1
            if (Math.abs(i - nums[i]) > 1) {
                return false; // If it is, then it's not an ideal permutation
            }
        }
        return true; // If we never found such a case, then it is an ideal permutation
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(isIdealPermutation(nums));
    }
}
