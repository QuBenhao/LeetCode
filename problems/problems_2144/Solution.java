package problems.problems_2144;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumCost(int[] cost) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] cost = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(minimumCost(cost));
    }
}
