package problems.problems_62;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int uniquePaths(int m, int n) {
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] += dp[j - 1];
            }
        }
        return dp[n - 1];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int m = Integer.parseInt(inputJsonValues[0]);
		int n = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(uniquePaths(m, n));
    }
}
