package problems.problems_1886;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean findRotation(int[][] mat, int[][] target) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] mat = jsonArrayToInt2DArray(inputJsonValues[0]);
		int[][] target = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(findRotation(mat, target));
    }
}
