package problems.problems_3600;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxStability(int n, int[][] edges, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maxStability(n, edges, k));
    }
}
