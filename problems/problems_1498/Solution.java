package problems.problems_1498;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;

public class Solution extends BaseSolution {
    private static final int MOD = 1_000_000_007;

    public int numSubseq(int[] nums, int target) {
        int n = nums.length;
        Arrays.sort(nums);
        int[] power = new int[n];
        power[0] = 1;
        for (int i = 1; i < n; i++) {
            power[i] = power[i - 1] * 2 % MOD;
        }
        int left = 0, right = n - 1;
        int ans = 0;
        while (left <= right) {
            while (left <= right && nums[left] + nums[right] > target) {
                --right;
            }
            if (left <= right) {
                ans = (ans + power[right - left]) % MOD;
            }
            ++left;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        int target = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(numSubseq(nums, target));
    }
}
