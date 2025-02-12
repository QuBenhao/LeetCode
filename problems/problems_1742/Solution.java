package problems.problems_1742;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countBalls(int lowLimit, int highLimit) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int lowLimit = Integer.parseInt(inputJsonValues[0]);
		int highLimit = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(countBalls(lowLimit, highLimit));
    }
}
