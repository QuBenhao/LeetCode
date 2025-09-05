package problems.problems_3495;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minOperations(int[][] queries) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] queries = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(minOperations(queries));
    }
}
