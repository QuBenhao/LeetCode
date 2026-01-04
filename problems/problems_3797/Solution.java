package problems.problems_3797;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfRoutes(String[] grid, int d) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] grid = jsonArrayToStringArray(inputJsonValues[0]);
		int d = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(numberOfRoutes(grid, d));
    }
}
