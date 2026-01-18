package problems.problems_3812;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> minimumFlips(int n, int[][] edges, String start, String target) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		String start = jsonStringToString(inputJsonValues[2]);
		String target = jsonStringToString(inputJsonValues[3]);
        return JSON.toJSON(minimumFlips(n, edges, start, target));
    }
}
