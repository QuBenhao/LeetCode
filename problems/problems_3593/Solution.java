package problems.problems_3593;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minIncrease(int n, int[][] edges, int[] cost) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		int[] cost = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(minIncrease(n, edges, cost));
    }
}
