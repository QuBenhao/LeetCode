package problems.problems_3086;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minimumMoves(int[] nums, int k, int maxChanges) {
        List<Integer> pos = new ArrayList<>();
        int c = 0; // Length of consecutive ones in nums
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) continue;
            pos.add(i); // Record the positions of ones
            c = Math.max(c, 1);
            if (i > 0 && nums[i - 1] == 1) {
                if (i > 1 && nums[i - 2] == 1) {
                    c = 3; // There are 3 consecutive ones
                } else {
                    c = Math.max(c, 2); // There are 2 consecutive ones
                }
            }
        }

        c = Math.min(c, k);
        if (maxChanges >= k - c) {
            // Each of the remaining k-c ones can be obtained in two operations
            return Math.max(c - 1, 0) + (k - c) * 2;
        }

        int n = pos.size();
        long[] sum = new long[n + 1];
        for (int i = 0; i < n; i++) {
            sum[i + 1] = sum[i] + pos.get(i);
        }

        long ans = Long.MAX_VALUE;
        // maxChanges ones can each be obtained in two operations; the rest must be moved to pos[i] one step at a time
        int size = k - maxChanges;
        for (int right = size; right <= n; right++) {
            // s1+s2 is the sum of distances from every pos[j], for j in [left, right), to index=pos[(left+right)/2]
            int left = right - size;
            int i = left + size / 2;
            long index = pos.get(i);
            long s1 = index * (i - left) - (sum[i] - sum[left]);
            long s2 = sum[right] - sum[i] - index * (right - i);
            ans = Math.min(ans, s1 + s2);
        }
        return ans + maxChanges * 2;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int maxChanges = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(minimumMoves(nums, k, maxChanges));
    }
}
