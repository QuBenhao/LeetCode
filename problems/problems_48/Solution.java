package problems.problems_48;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public void rotate(int[][] matrix) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] matrix = jsonArrayToInt2DArray(inputJsonValues[0]);
		rotate(matrix);
        return JSON.toJSON(matrix);
    }
}
