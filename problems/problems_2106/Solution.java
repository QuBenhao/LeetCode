package problems.problems_2106;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxTotalFruits(int[][] fruits, int startPos, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] fruits = jsonArrayToInt2DArray(inputJsonValues[0]);
		int startPos = Integer.parseInt(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maxTotalFruits(fruits, startPos, k));
    }
}
