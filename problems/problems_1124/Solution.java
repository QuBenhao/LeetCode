package problems.problems_1124;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int longestWPI(int[] hours) {
        int ans = 0;
        int n = hours.length;
        int prefixSum = 0;
        Map<Integer, Integer> firstOccurrence = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            prefixSum += (hours[i] > 8 ? 1 : -1);
            if (prefixSum > 0) {
                ans = i + 1; // All hours are good
            } else {
                // If we have seen this prefix sum before, it means we can find a subarray
                // that has a positive sum
                if (firstOccurrence.containsKey(prefixSum - 1)) {
                    ans = Math.max(ans, i - firstOccurrence.get(prefixSum - 1));
                }
            }
            // Store the first occurrence of this prefix sum
            firstOccurrence.putIfAbsent(prefixSum, i);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] hours = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(longestWPI(hours));
    }
}
