package problems.problems_3584;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maximumProduct(int[] nums, int m) {
        int n = nums.length;
        int[] preMax = new int[n], preMin = new int[n];
        preMax[0] = preMin[0] = nums[0];
        long ans = Long.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                preMax[i] = Math.max(preMax[i - 1], nums[i]);
                preMin[i] = Math.min(preMin[i - 1], nums[i]);
            }
            if (i - m + 1 >= 0) {
                ans = Math.max(ans, (long)preMax[i-m+1] *nums[i]);
                ans = Math.max(ans, (long)preMin[i-m+1] * nums[i]);
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int m = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maximumProduct(nums, m));
    }
}
