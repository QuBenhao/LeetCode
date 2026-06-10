package problems.problems_3558;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int assignEdgeWeights(int[][] edges) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] edges = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(assignEdgeWeights(edges));
    }
}
