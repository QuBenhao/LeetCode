package problems.problems_1235;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int binarySearch(Integer[] idxes, int[] endTime, int right, int target) {
        int left = 0;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (endTime[idxes[mid]] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    public int jobScheduling(int[] startTime, int[] endTime, int[] profit) {
        int n = startTime.length;
        Integer[] idxes = new Integer[n];
        for (int i = 0; i < n; i++) {
            idxes[i] = i;
        }
        Arrays.sort(idxes, Comparator.comparingInt(a -> endTime[a]));
        int[] dp = new int[n+1];
        for (int i = 0; i < n; i++) {
            int p = binarySearch(idxes, endTime, i, startTime[idxes[i]]);
            dp[i + 1] = Math.max(dp[i], dp[p] + profit[idxes[i]]);
        }
        return dp[n];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] startTime = jsonArrayToIntArray(inputJsonValues[0]);
		int[] endTime = jsonArrayToIntArray(inputJsonValues[1]);
		int[] profit = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(jobScheduling(startTime, endTime, profit));
    }
}
