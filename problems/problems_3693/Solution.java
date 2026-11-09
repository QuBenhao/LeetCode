package problems.problems_3693;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int climbStairs(int n, int[] costs) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[] costs = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(climbStairs(n, costs));
    }
}
