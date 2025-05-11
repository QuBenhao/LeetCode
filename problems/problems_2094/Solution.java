package problems.problems_2094;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] findEvenNumbers(int[] digits) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] digits = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(findEvenNumbers(digits));
    }
}
