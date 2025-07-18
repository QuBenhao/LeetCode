package problems.problems_2163;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minimumDifference(int[] nums) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int n = nums.length / 3;
        long suffixSum = 0;
        for (int i = 2 * n; i < nums.length; ++i) {
            suffixSum += nums[i];
            pq.offer(nums[i]);
        }
        long[] suffixMax = new long[n + 1];
        suffixMax[n] = suffixSum;
        for (int i = 2 * n - 1; i >= n; --i) {
            pq.offer(nums[i]);
            suffixSum += nums[i] - pq.poll();
            suffixMax[i - n] = suffixSum;
        }
        long prefixSum = 0;
        pq.clear();
        for (int i = 0; i < n; ++i) {
            prefixSum += nums[i];
            pq.offer(-nums[i]);
        }
        long ans = prefixSum - suffixMax[0];
        for (int i = n; i < 2 * n; ++i) {
            pq.offer(-nums[i]);
            prefixSum += nums[i] + pq.poll();
            ans = Math.min(ans, prefixSum - suffixMax[i - n + 1]);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(minimumDifference(nums));
    }
}
