package problems.problems_3453;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double separateSquares(int[][] squares) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] squares = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(separateSquares(squares));
    }
}
