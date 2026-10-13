package problems.problems_3723;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String maxSumOfSquares(int num, int sum) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int num = Integer.parseInt(inputJsonValues[0]);
		int sum = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxSumOfSquares(num, sum));
    }
}
