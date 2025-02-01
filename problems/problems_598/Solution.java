package problems.problems_598;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxCount(int m, int n, int[][] ops) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int m = Integer.parseInt(inputJsonValues[0]);
		int n = Integer.parseInt(inputJsonValues[1]);
		int[][] ops = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(maxCount(m, n, ops));
    }
}
