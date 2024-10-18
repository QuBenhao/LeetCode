package problems.problems_3191;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minOperations(int[] nums) {
        int ans = 0, n = nums.length;
        for (int i = 0; i < n - 2; i++) {
            if (nums[i] == 0) {
                ans++;
                nums[i + 1] ^= 1;
                nums[i + 2] ^= 1;
            }
        }
        return nums[n - 2] == 1 && nums[n - 1] == 1 ? ans : -1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(minOperations(nums));
    }
}
