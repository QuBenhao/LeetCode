package problems.problems_3603;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minCost(int m, int n, int[][] waitCost) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int m = Integer.parseInt(inputJsonValues[0]);
		int n = Integer.parseInt(inputJsonValues[1]);
		int[][] waitCost = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(minCost(m, n, waitCost));
    }
}
