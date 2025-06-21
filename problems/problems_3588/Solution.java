package problems.problems_3588;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maxArea(int[][] coords) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] coords = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(maxArea(coords));
    }
}
