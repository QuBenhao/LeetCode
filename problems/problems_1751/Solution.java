package problems.problems_1751;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int binarySearch(int[][] events, int right, int end) {
        int left = 0;
        while (left < right) {
            int mid = (left + right) / 2;
            if (events[mid][1] < end) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    public int maxValue(int[][] events, int k) {
        Arrays.sort(events, Comparator.comparingInt(a -> a[1]));
        int n = events.length;
        int[][] dp = new int[n + 1][k + 1];
        for (int i = 0; i < n; i++) {
            int p = binarySearch(events, i, events[i][0]);
            for (int j = 1; j <= k; j++) {
                dp[i + 1][j] = Math.max(dp[i][j], dp[p][j - 1] + events[i][2]);
            }
        }
        return dp[n][k];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] events = jsonArrayToInt2DArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxValue(events, k));
    }
}
