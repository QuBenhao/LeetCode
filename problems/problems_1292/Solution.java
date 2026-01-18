package problems.problems_1292;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxSideLength(int[][] mat, int threshold) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] mat = jsonArrayToInt2DArray(inputJsonValues[0]);
		int threshold = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxSideLength(mat, threshold));
    }
}
