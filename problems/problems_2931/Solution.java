package problems.problems_2931;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maxSpending(int[][] values) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] values = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(maxSpending(values));
    }
}
