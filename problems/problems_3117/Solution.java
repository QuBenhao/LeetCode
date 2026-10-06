package problems.problems_3117;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumValueSum(int[] nums, int[] andValues) {
        Map<Long, Integer> memo = new HashMap<>();
        int ans = dfs(0, 0, -1, nums, andValues, memo);
        return ans < Integer.MAX_VALUE / 2 ? ans : -1;
    }

    private int dfs(int i, int j, int and, int[] nums, int[] andValues, Map<Long, Integer> memo) {
        int n = nums.length;
        int m = andValues.length;
        if (n - i < m - j) { // Not enough elements remain
            return Integer.MAX_VALUE / 2; // Divide by 2 to prevent overflow in + nums[i] below
        }
        if (j == m) { // Split into m segments
            return i == n ? 0 : Integer.MAX_VALUE / 2;
        }
        and &= nums[i];
        // Pack the three parameters into one long
        long mask = (long) i << 36 | (long) j << 32 | and;
        if (memo.containsKey(mask)) { // Already computed
            return memo.get(mask);
        }
        int res = dfs(i + 1, j, and, nums, andValues, memo); // Do not split here
        if (and == andValues[j]) { // Split here; nums[i] is the last number in this segment
            res = Math.min(res, dfs(i + 1, j + 1, -1, nums, andValues, memo) + nums[i]);
        }
        memo.put(mask, res); // Memoization
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int[] andValues = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minimumValueSum(nums, andValues));
    }
}
