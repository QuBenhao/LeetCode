package problems.problems_3652;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maxProfit(int[] prices, int[] strategy, int k) {
        int n = prices.length;
        long[] preSum = new long[n + 1], originalPreSum = new long[n + 1];
        for (int i = 0; i < n; i++) {
            preSum[i + 1] = preSum[i] + prices[i] * strategy[i];
            originalPreSum[i + 1] = originalPreSum[i] + prices[i];
        }
        long ans = 0;
        for (int i = 0; i <= n - k; ++i) {
            long cur = preSum[i] - preSum[i + k];
            cur += originalPreSum[i + k] - originalPreSum[i + k/2];
            ans = Math.max(ans, cur);
        }
        return ans + preSum[n];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] prices = jsonArrayToIntArray(inputJsonValues[0]);
		int[] strategy = jsonArrayToIntArray(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maxProfit(prices, strategy, k));
    }
}
