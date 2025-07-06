package problems.problems_3607;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] processQueries(int c, int[][] connections, int[][] queries) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int c = Integer.parseInt(inputJsonValues[0]);
		int[][] connections = jsonArrayToInt2DArray(inputJsonValues[1]);
		int[][] queries = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(processQueries(c, connections, queries));
    }
}
