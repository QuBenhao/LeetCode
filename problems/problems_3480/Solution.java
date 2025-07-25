package problems.problems_3480;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maxSubarrays(int n, int[][] conflictingPairs) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] conflictingPairs = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(maxSubarrays(n, conflictingPairs));
    }
}
