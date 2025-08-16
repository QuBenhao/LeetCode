package problems.problems_837;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double new21Game(int n, int k, int maxPts) {
        double[] dp = new double[n + 1];
        double s = 0.0;
        for (int i = n; i >= 0; --i) {
            dp[i] = i >= k ? 1.0 : s / maxPts;
            s += dp[i];
            if (i + maxPts <= n) {
                s -= dp[i + maxPts];
            }
        }
        return dp[0];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int maxPts = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(new21Game(n, k, maxPts));
    }
}
