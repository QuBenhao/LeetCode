package problems.problems_1840;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxBuilding(int n, int[][] restrictions) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] restrictions = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(maxBuilding(n, restrictions));
    }
}
