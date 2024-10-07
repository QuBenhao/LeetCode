package problems.problems_871;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minRefuelStops(int target, int startFuel, int[][] stations) {
        int n = stations.length;
        int[] dp = new int[n + 1];
        dp[0] = startFuel;
        for (int i = 0; i < n; ++i) {
            for (int t = i; t >= 0; --t) {
                if (dp[t] >= stations[i][0]) {
                    dp[t + 1] = Math.max(dp[t + 1], dp[t] + stations[i][1]);
                }
            }
        }
        for (int i = 0; i <= n; ++i) {
            if (dp[i] >= target) {
                return i;
            }
        }
        return -1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int target = Integer.parseInt(inputJsonValues[0]);
		int startFuel = Integer.parseInt(inputJsonValues[1]);
		int[][] stations = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(minRefuelStops(target, startFuel, stations));
    }
}
