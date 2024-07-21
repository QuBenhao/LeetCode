package problems.problems_121;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxProfit(int[] prices) {
        int buy = -prices[0], sell = 0;
        for (int i = 1; i < prices.length; i++) {
            buy = Math.max(buy, -prices[i]);
            sell = Math.max(sell, buy + prices[i]);
        }
        return sell;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] prices = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxProfit(prices));
    }
}
