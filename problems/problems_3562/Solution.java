package problems.problems_3562;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxProfit(int n, int[] present, int[] future, int[][] hierarchy, int budget) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[] present = jsonArrayToIntArray(inputJsonValues[1]);
		int[] future = jsonArrayToIntArray(inputJsonValues[2]);
		int[][] hierarchy = jsonArrayToInt2DArray(inputJsonValues[3]);
		int budget = Integer.parseInt(inputJsonValues[4]);
        return JSON.toJSON(maxProfit(n, present, future, hierarchy, budget));
    }
}
