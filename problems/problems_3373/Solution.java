package problems.problems_3373;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] maxTargetNodes(int[][] edges1, int[][] edges2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] edges1 = jsonArrayToInt2DArray(inputJsonValues[0]);
		int[][] edges2 = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(maxTargetNodes(edges1, edges2));
    }
}
