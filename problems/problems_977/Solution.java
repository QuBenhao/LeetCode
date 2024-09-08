package problems.problems_977;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] sortedSquares(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        for (int left = 0, right = n - 1, pos = n - 1; left <= right; pos--) {
            if (nums[left] * nums[left] > nums[right] * nums[right]) {
                ans[pos] = nums[left] * nums[left];
                left++;
            } else {
                ans[pos] = nums[right] * nums[right];
                right--;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(sortedSquares(nums));
    }
}
