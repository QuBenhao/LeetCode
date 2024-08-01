package problems.problems_322;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int coinChange(int[] coins, int amount) {
        int[] dp = new int[amount + 1];
        Arrays.fill(dp, amount + 1);
        dp[0] = 0;
        for (int i = 1; i <= amount; i++) {
            for (int coin : coins) {
                if (coin <= i) {
                    dp[i] = Math.min(dp[i], dp[i - coin] + 1);
                }
            }
        }
        return dp[amount] == amount + 1 ? -1 : dp[amount];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] coins = jsonArrayToIntArray(inputJsonValues[0]);
		int amount = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(coinChange(coins, amount));
    }
}
