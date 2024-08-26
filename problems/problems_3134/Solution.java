package problems.problems_3134;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int medianOfUniquenessArray(int[] nums) {
        int n = nums.length;
        long k = ((long)n * (n + 1) / 2 + 1) / 2;
        int left = 1, right = n;
        while (left < right) {
            int mid = left + right >> 1;
            if (check(nums, k, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private boolean check(int[] nums, long k, int upper) {
        long count = 0L;
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int l = 0, r = 0; r < nums.length; r++) {
            cnt.put(nums[r], cnt.getOrDefault(nums[r], 0) + 1);
            while (cnt.size() > upper) {
                cnt.put(nums[l], cnt.get(nums[l]) - 1);
                if (cnt.get(nums[l]) == 0) {
                    cnt.remove(nums[l]);
                }
                l++;
            }
            count += r - l + 1;
            if (count >= k) {
                return true;
            }
        }
        return false;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(medianOfUniquenessArray(nums));
    }
}
