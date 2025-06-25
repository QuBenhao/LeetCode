package problems.problems_1802;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxValue(int n, int index, int maxSum) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int index = Integer.parseInt(inputJsonValues[1]);
		int maxSum = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maxValue(n, index, maxSum));
    }
}
