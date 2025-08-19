package problems.problems_1277;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countSquares(int[][] matrix) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] matrix = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(countSquares(matrix));
    }
}
