package problems.problems_3171;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumDifference(int[] nums, int k) {
        int ans = Math.abs(nums[0] - k);
        int n = nums.length;
        for (int i = 1; i < n; i++) {
            ans = Math.min(ans, Math.abs(nums[i] - k));
            for (int j = i - 1; j >= 0 && (nums[j] | nums[i]) != nums[j]; j--) {
                nums[j] |= nums[i];
                ans = Math.min(ans, Math.abs(nums[j] - k));
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minimumDifference(nums, k));
    }
}
