package problems.problems_1857;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int largestPathValue(String colors, int[][] edges) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String colors = jsonStringToString(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(largestPathValue(colors, edges));
    }
}
