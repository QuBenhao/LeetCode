package problems.problems_70;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int climbStairs(int n) {
        int[] dp = new int[3];
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i <= n; i++) {
            dp[i % 3] = dp[(i - 1) % 3] + dp[(i - 2) % 3];
        }
        return dp[n % 3];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(climbStairs(n));
    }
}
