package problems.problems_3363;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxCollectedFruits(int[][] fruits) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] fruits = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(maxCollectedFruits(fruits));
    }
}
