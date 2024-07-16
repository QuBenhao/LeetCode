package problems.problems_2959;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfSets(int n, int maxDistance, int[][] roads) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int maxDistance = Integer.parseInt(inputJsonValues[1]);
		int[][] roads = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(numberOfSets(n, maxDistance, roads));
    }
}
