package problems.problems_2492;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minScore(int n, int[][] roads) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] roads = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(minScore(n, roads));
    }
}
