package problems.problems_2561;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minCost(int[] basket1, int[] basket2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] basket1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] basket2 = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minCost(basket1, basket2));
    }
}
