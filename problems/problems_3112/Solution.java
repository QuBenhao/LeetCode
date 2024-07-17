package problems.problems_3112;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] minimumTime(int n, int[][] edges, int[] disappear) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		int[] disappear = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(minimumTime(n, edges, disappear));
    }
}
