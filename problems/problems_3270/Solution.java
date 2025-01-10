package problems.problems_3270;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int generateKey(int num1, int num2, int num3) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int num1 = Integer.parseInt(inputJsonValues[0]);
		int num2 = Integer.parseInt(inputJsonValues[1]);
		int num3 = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(generateKey(num1, num2, num3));
    }
}
