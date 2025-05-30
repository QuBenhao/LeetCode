package problems.problems_LCR_091;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minCost(int[][] costs) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] costs = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(minCost(costs));
    }
}
