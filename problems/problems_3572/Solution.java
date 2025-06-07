package problems.problems_3572;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxSumDistinctTriplet(int[] x, int[] y) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] x = jsonArrayToIntArray(inputJsonValues[0]);
		int[] y = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(maxSumDistinctTriplet(x, y));
    }
}
