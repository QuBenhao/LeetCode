package problems.problems_3464;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxDistance(int side, int[][] points, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int side = Integer.parseInt(inputJsonValues[0]);
		int[][] points = jsonArrayToInt2DArray(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maxDistance(side, points, k));
    }
}
