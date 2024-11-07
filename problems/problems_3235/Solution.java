package problems.problems_3235;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canReachCorner(int xCorner, int yCorner, int[][] circles) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int xCorner = Integer.parseInt(inputJsonValues[0]);
		int yCorner = Integer.parseInt(inputJsonValues[1]);
		int[][] circles = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(canReachCorner(xCorner, yCorner, circles));
    }
}
