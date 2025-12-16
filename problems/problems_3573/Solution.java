package problems.problems_3573;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maximumProfit(int[] prices, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] prices = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maximumProfit(prices, k));
    }
}
