package problems.problems_1578;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minCost(String colors, int[] neededTime) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String colors = jsonStringToString(inputJsonValues[0]);
		int[] neededTime = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minCost(colors, neededTime));
    }
}
