package problems.problems_3115;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumPrimeDifference(int[] nums) {
        int left = 0, right = nums.length - 1;
        while (left < right && !isPrime(nums[left])) {
            left++;
        }
        while (left < right && !isPrime(nums[right])) {
            right--;
        }
        return right - left;
    }

    private boolean isPrime(int n) {
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return n >= 2;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maximumPrimeDifference(nums));
    }
}
