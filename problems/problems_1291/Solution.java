package problems.problems_1291;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> sequentialDigits(int low, int high) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int low = Integer.parseInt(inputJsonValues[0]);
		int high = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(sequentialDigits(low, high));
    }
}
