package problems.problems_121;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxProfit(int[] prices) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] prices = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxProfit(prices));
    }
}
