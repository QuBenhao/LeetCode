package problems.problems_3796;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findMaxVal(int n, int[][] restrictions, int[] diff) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] restrictions = jsonArrayToInt2DArray(inputJsonValues[1]);
		int[] diff = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(findMaxVal(n, restrictions, diff));
    }
}
