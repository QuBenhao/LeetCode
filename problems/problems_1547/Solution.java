package problems.problems_1547;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minCost(int n, int[] cuts) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[] cuts = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minCost(n, cuts));
    }
}
