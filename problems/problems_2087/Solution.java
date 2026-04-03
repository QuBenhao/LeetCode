package problems.problems_2087;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minCost(int[] startPos, int[] homePos, int[] rowCosts, int[] colCosts) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] startPos = jsonArrayToIntArray(inputJsonValues[0]);
		int[] homePos = jsonArrayToIntArray(inputJsonValues[1]);
		int[] rowCosts = jsonArrayToIntArray(inputJsonValues[2]);
		int[] colCosts = jsonArrayToIntArray(inputJsonValues[3]);
        return JSON.toJSON(minCost(startPos, homePos, rowCosts, colCosts));
    }
}
