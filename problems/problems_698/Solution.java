package problems.problems_698;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int n = nums.length;
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        if (sum % k != 0) {
            return false;
        }
        int target = sum / k;
        for (int num : nums) {
            if (num > target) {
                return false;
            }
        }
        int allPicked = (1 << n) - 1;
        int[] dp = new int[1 << n];
        Arrays.fill(dp, -1);
        dp[0] = 0;
        for (int mask = 0; mask < 1 << n; mask++) {
            for (int i = 0; i < n; i++) {
                if (((mask >> i) & 1) != 0) {
                    int before = mask ^ (1 << i);
                    if (dp[before] != -1 && dp[before] + nums[i] <= target) {
                        dp[mask] = (dp[before] + nums[i]) % target;
                    }
                }
            }
        }
        return dp[allPicked] == 0;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(canPartitionKSubsets(nums, k));
    }
}
