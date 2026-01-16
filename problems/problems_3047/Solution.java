package problems.problems_3047;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long largestSquareArea(int[][] bottomLeft, int[][] topRight) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] bottomLeft = jsonArrayToInt2DArray(inputJsonValues[0]);
		int[][] topRight = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(largestSquareArea(bottomLeft, topRight));
    }
}
