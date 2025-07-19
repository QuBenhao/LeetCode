package problems.problems_3620;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findMaxPathScore(int[][] edges, boolean[] online, long k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] edges = jsonArrayToInt2DArray(inputJsonValues[0]);
		boolean[] online = jsonArrayToBooleanArray(inputJsonValues[1]);
		long k = Long.parseLong(inputJsonValues[2]);
        return JSON.toJSON(findMaxPathScore(edges, online, k));
    }
}
