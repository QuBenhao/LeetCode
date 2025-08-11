package problems.problems_2787;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfWays(int n, int x) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int x = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(numberOfWays(n, x));
    }
}
