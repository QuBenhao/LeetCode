package problems.problems_2065;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximalPathQuality(int[] values, int[][] edges, int maxTime) {

    }

    @Override
    public Object solve(String[] values) {
        int[] values = jsonArrayToIntArray(values[0]);
		int[][] edges = jsonArrayToInt2DArray(values[1]);
		int maxTime = Integer.parseInt(values[2]);
        return JSON.toJSON(maximalPathQuality(values, edges, maxTime));
    }
}
