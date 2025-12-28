package problems.problems_3791;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long countBalanced(long low, long high) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        long low = Long.parseLong(inputJsonValues[0]);
		long high = Long.parseLong(inputJsonValues[1]);
        return JSON.toJSON(countBalanced(low, high));
    }
}
