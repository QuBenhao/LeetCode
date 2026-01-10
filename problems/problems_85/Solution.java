package problems.problems_85;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximalRectangle(char[][] matrix) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[][] matrix = jsonArrayToChar2DArray(inputJsonValues[0]);
        return JSON.toJSON(maximalRectangle(matrix));
    }
}
