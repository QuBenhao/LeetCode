package problems.problems_2169;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countOperations(int num1, int num2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int num1 = Integer.parseInt(inputJsonValues[0]);
		int num2 = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(countOperations(num1, num2));
    }
}
