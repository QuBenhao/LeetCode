package problems.problems_3800;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minimumCost(String s, String t, int flipCost, int swapCost, int crossCost) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		String t = jsonStringToString(inputJsonValues[1]);
		int flipCost = Integer.parseInt(inputJsonValues[2]);
		int swapCost = Integer.parseInt(inputJsonValues[3]);
		int crossCost = Integer.parseInt(inputJsonValues[4]);
        return JSON.toJSON(minimumCost(s, t, flipCost, swapCost, crossCost));
    }
}
