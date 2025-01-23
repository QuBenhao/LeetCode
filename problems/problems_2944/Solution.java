package problems.problems_2944;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumCoins(int[] prices) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] prices = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(minimumCoins(prices));
    }
}
