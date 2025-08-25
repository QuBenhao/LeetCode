package problems.problems_3000;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] dimensions = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(areaOfMaxDiagonal(dimensions));
    }
}
