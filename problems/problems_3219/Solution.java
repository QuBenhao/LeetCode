package problems.problems_3219;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minimumCost(int m, int n, int[] horizontalCut, int[] verticalCut) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int m = Integer.parseInt(inputJsonValues[0]);
		int n = Integer.parseInt(inputJsonValues[1]);
		int[] horizontalCut = jsonArrayToIntArray(inputJsonValues[2]);
		int[] verticalCut = jsonArrayToIntArray(inputJsonValues[3]);
        return JSON.toJSON(minimumCost(m, n, horizontalCut, verticalCut));
    }
}
