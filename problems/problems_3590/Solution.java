package problems.problems_3590;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] kthSmallest(int[] par, int[] vals, int[][] queries) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] par = jsonArrayToIntArray(inputJsonValues[0]);
		int[] vals = jsonArrayToIntArray(inputJsonValues[1]);
		int[][] queries = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(kthSmallest(par, vals, queries));
    }
}
