package problems.problems_3784;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minCost(String s, int[] cost) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		int[] cost = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minCost(s, cost));
    }
}
