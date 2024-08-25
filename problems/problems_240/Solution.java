package problems.problems_240;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean searchMatrix(int[][] matrix, int target) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] matrix = jsonArrayToInt2DArray(inputJsonValues[0]);
		int target = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(searchMatrix(matrix, target));
    }
}
