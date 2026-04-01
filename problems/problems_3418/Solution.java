package problems.problems_3418;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumAmount(int[][] coins) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] coins = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(maximumAmount(coins));
    }
}
