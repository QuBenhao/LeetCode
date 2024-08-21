package problems.problems_LCR_088;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int[] dp = new int[3];
        for (int i = 2; i <= n; i++) {
            dp[i % 3] = Math.min(dp[(i - 1) % 3] + cost[i - 1], dp[(i - 2) % 3] + cost[i - 2]);
        }
        return dp[n % 3];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] cost = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(minCostClimbingStairs(cost));
    }
}
