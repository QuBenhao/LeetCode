package problems.problems_983;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int mincostTickets(int[] days, int[] costs) {
        int n = days.length;
        int[] dp = new int[n + 1];
        dp[0] = 0;
        for (int i = 0, j = 0, k = 0; i < n; i++) {
            while (days[j] <= days[i] - 7) {
                j++;
            }
            while (days[k] <= days[i] - 30) {
                k++;
            }
            dp[i + 1] = Math.min(dp[i] + costs[0], Math.min(dp[j] + costs[1], dp[k] + costs[2]));
        }
        return dp[n];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] days = jsonArrayToIntArray(inputJsonValues[0]);
		int[] costs = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(mincostTickets(days, costs));
    }
}
