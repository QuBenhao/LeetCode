package problems.problems_2747;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] countServers(int n, int[][] logs, int x, int[] queries) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] logs = jsonArrayToInt2DArray(inputJsonValues[1]);
		int x = Integer.parseInt(inputJsonValues[2]);
		int[] queries = jsonArrayToIntArray(inputJsonValues[3]);
        return JSON.toJSON(countServers(n, logs, x, queries));
    }
}
