package problems.problems_3102;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumDistance(int[][] points) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] points = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(minimumDistance(points));
    }
}
