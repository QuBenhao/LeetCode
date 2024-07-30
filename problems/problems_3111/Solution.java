package problems.problems_3111;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minRectanglesToCoverPoints(int[][] points, int w) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] points = jsonArrayToInt2DArray(inputJsonValues[0]);
		int w = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minRectanglesToCoverPoints(points, w));
    }
}
