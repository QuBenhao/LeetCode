package problems.problems_2787;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int MOD = 1_000_000_007;
    public int numberOfWays(int n, int x) {
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            long v = (long) Math.pow(i, x);
            if (v > n) {
                break;
            }
            for (int j = n; j >= (int)v; j--) {
                dp[j] = (dp[j] + dp[j - (int)v]) % MOD;
            }
        }
        return dp[n];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int x = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(numberOfWays(n, x));
    }
}
