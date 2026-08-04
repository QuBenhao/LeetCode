package problems.problems_3310;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> remainingMethods(int n, int k, int[][] invocations) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int[][] invocations = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(remainingMethods(n, k, invocations));
    }
}
