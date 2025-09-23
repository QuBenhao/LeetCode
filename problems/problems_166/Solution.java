package problems.problems_166;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String fractionToDecimal(int numerator, int denominator) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int numerator = Integer.parseInt(inputJsonValues[0]);
		int denominator = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(fractionToDecimal(numerator, denominator));
    }
}
