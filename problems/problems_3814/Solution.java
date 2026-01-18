package problems.problems_3814;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxCapacity(int[] costs, int[] capacity, int budget) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] costs = jsonArrayToIntArray(inputJsonValues[0]);
		int[] capacity = jsonArrayToIntArray(inputJsonValues[1]);
		int budget = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maxCapacity(costs, capacity, budget));
    }
}
