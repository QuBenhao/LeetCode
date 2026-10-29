package problems.problems_3970;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int shortestPath(int n, int[][] edges, String labels, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		String labels = jsonStringToString(inputJsonValues[2]);
		int k = Integer.parseInt(inputJsonValues[3]);
        return JSON.toJSON(shortestPath(n, edges, labels, k));
    }
}
