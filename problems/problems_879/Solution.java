package problems.problems_879;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int MOD = 1000000007;
    public int profitableSchemes(int n, int minProfit, int[] group, int[] profit) {
        int ans = minProfit == 0 ? 1 : 0;
        int[][] dp = new int[n + 1][minProfit + 1];
        dp[0][0] = 1;
        for (int i = 0; i < group.length; ++i) {
            int g = group[i], p = profit[i];
            for (int j = n; j >= g; --j) {
                for (int k = minProfit; k >= 0; --k) {
                    int newProfit = Math.min(minProfit, k + p);
                    dp[j][newProfit] = (dp[j][newProfit] + dp[j - g][k]) % MOD;
                    if (newProfit == minProfit) {
                        ans = (ans + dp[j - g][k]) % MOD;
                    }
                }
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int minProfit = Integer.parseInt(inputJsonValues[1]);
		int[] group = jsonArrayToIntArray(inputJsonValues[2]);
		int[] profit = jsonArrayToIntArray(inputJsonValues[3]);
        return JSON.toJSON(profitableSchemes(n, minProfit, group, profit));
    }
}
