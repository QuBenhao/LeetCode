package problems.problems_910;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int smallestRangeII(int[] nums, int k) {
        Arrays.sort(nums);
        int n = nums.length;
        int ans = nums[n - 1] - nums[0];
        for (int i = 1; i < n; i++) {
            int mx = Math.max(nums[i - 1] + k, nums[n - 1] - k);
            int mn = Math.min(nums[0] + k, nums[i] - k);
            ans = Math.min(ans, mx - mn);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(smallestRangeII(nums, k));
    }
}
