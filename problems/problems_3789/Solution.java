package problems.problems_3789;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minimumCost(int cost1, int cost2, int costBoth, int need1, int need2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int cost1 = Integer.parseInt(inputJsonValues[0]);
		int cost2 = Integer.parseInt(inputJsonValues[1]);
		int costBoth = Integer.parseInt(inputJsonValues[2]);
		int need1 = Integer.parseInt(inputJsonValues[3]);
		int need2 = Integer.parseInt(inputJsonValues[4]);
        return JSON.toJSON(minimumCost(cost1, cost2, costBoth, need1, need2));
    }
}
