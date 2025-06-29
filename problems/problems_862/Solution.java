package problems.problems_862;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int shortestSubarray(int[] nums, int k) {
        Deque<long[]> dq = new ArrayDeque<>();
        int ans = Integer.MAX_VALUE;
        int n = nums.length;
        dq.add(new long[]{0, -1});  // (sum, index)
        long prefixSum = 0;
        for (int i = 0; i < n; ++i) {
            prefixSum += nums[i];
            while (!dq.isEmpty() && prefixSum - dq.peekFirst()[0] >= k) {
                ans = Math.min(ans, i - (int)dq.pollFirst()[1]);
            }
            while (!dq.isEmpty() && prefixSum <= dq.peekLast()[0]) {
                dq.pollLast();
            }
            dq.add(new long[]{prefixSum, i});
        }
        return ans == Integer.MAX_VALUE ? -1 : ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(shortestSubarray(nums, k));
    }
}
