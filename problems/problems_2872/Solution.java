package problems.problems_2872;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxKDivisibleComponents(int n, int[][] edges, int[] values, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		int[] values = jsonArrayToIntArray(inputJsonValues[2]);
		int k = Integer.parseInt(inputJsonValues[3]);
        return JSON.toJSON(maxKDivisibleComponents(n, edges, values, k));
    }
}
