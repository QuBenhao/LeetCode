package problems.problems_1563;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int stoneGameV(int[] stoneValue) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] stoneValue = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(stoneGameV(stoneValue));
    }
}
