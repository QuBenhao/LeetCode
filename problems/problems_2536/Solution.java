package problems.problems_2536;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[][] rangeAddQueries(int n, int[][] queries) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] queries = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(rangeAddQueries(n, queries));
    }
}
