package problems.problems_2576;

import java.util.Arrays;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxNumOfMarkedIndices(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length, left = 0;
        for (int right = (n + 1) / 2; right < n; right++) {
            if (nums[right] >= 2 * nums[left]) {
                left++;
            }
        }
        return left * 2;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxNumOfMarkedIndices(nums));
    }
}
