package problems.problems_1928;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minCost(int maxTime, int[][] edges, int[] passingFees) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int maxTime = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		int[] passingFees = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(minCost(maxTime, edges, passingFees));
    }
}
