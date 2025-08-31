package problems.problems_1792;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double maxAverageRatio(int[][] classes, int extraStudents) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] classes = jsonArrayToInt2DArray(inputJsonValues[0]);
		int extraStudents = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxAverageRatio(classes, extraStudents));
    }
}
