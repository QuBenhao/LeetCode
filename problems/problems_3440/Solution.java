package problems.problems_3440;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxFreeTime(int eventTime, int[] startTime, int[] endTime) {
        int n = startTime.length;
        int[] distances = new int[n + 1];
        distances[0] = startTime[0];
        for (int i = 1; i < n; ++i) {
            distances[i] = startTime[i] - endTime[i - 1];
        }
        distances[n] = eventTime - endTime[n - 1];

        int a = -1, b = -1, c = -1;
        for (int i = 0; i <= n; ++i) {
            if (a == -1 || distances[i] >= distances[a]) {
                c = b;
                b = a;
                a = i;
            } else if (b == -1 || distances[i] >= distances[b]) {
                c = b;
                b = i;
            } else if (c == -1 || distances[i] >= distances[c]) {
                c = i;
            }
        }

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int cur = endTime[i] - startTime[i];
            if ((a != i && a != i + 1 && distances[a] >= cur) ||
                (b != i && b != i + 1 && distances[b] >= cur) ||
                distances[c] >= cur) {
                ans = Math.max(ans, distances[i] + distances[i + 1] + cur);
            } else {
                ans = Math.max(ans, distances[i] + distances[i + 1]);
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int eventTime = Integer.parseInt(inputJsonValues[0]);
		int[] startTime = jsonArrayToIntArray(inputJsonValues[1]);
		int[] endTime = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(maxFreeTime(eventTime, startTime, endTime));
    }
}
