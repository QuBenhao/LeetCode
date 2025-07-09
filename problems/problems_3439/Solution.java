package problems.problems_3439;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxFreeTime(int eventTime, int k, int[] startTime, int[] endTime) {
        int n = startTime.length;
        int[] dist = new int[n + 1];
        dist[0] = startTime[0];
        dist[n] = eventTime - endTime[n - 1];
        int cur = dist[0];
        for (int i = 1; i <= k; ++i) {
            if (i < n) {
                dist[i] = startTime[i] - endTime[i - 1];
            }
            cur += dist[i];
        }
        int ans = cur;
        for (int i = k + 1; i <= n; ++i) {
            if (i < n) {
                dist[i] = startTime[i] - endTime[i - 1];
            }
            cur += dist[i] - dist[i - k - 1];
            ans = Math.max(ans, cur);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int eventTime = Integer.parseInt(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int[] startTime = jsonArrayToIntArray(inputJsonValues[2]);
		int[] endTime = jsonArrayToIntArray(inputJsonValues[3]);
        return JSON.toJSON(maxFreeTime(eventTime, k, startTime, endTime));
    }
}
