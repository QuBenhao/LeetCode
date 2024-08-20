package problems.problems_LCR_088;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minCostClimbingStairs(int[] cost) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] cost = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(minCostClimbingStairs(cost));
    }
}
