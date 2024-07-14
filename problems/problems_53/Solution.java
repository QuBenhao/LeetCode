package problems.problems_53;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int DivideAndConquer(int[] nums, int left, int right) {
        if (left == right) {
            return nums[left];
        }
        int mid = (left + right) / 2;
        int leftSum = DivideAndConquer(nums, left, mid);
        int rightSum = DivideAndConquer(nums, mid + 1, right);
        int crossSum = 0, leftCrossSum = nums[mid], rightCrossSum = 0;
        for (int i = mid; i >= left; i--) {
            crossSum += nums[i];
            leftCrossSum = Math.max(leftCrossSum, crossSum);
        }
        crossSum = 0;
        for (int i = mid + 1; i <= right; i++) {
            crossSum += nums[i];
            rightCrossSum = Math.max(rightCrossSum, crossSum);
        }
        return Math.max(Math.max(leftSum, rightSum), leftCrossSum + rightCrossSum);
    }

    public int maxSubArray(int[] nums) {
        return DivideAndConquer(nums, 0, nums.length - 1);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxSubArray(nums));
    }
}
