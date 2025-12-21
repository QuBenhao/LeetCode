package problems.problems_3786;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long interactionCosts(int n, int[][] edges, int[] group) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		int[] group = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(interactionCosts(n, edges, group));
    }
}
