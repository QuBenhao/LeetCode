package problems.problems_3143;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxPointsInsideSquare(int[][] points, String s) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] points = jsonArrayToInt2DArray(inputJsonValues[0]);
		String s = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(maxPointsInsideSquare(points, s));
    }
}
