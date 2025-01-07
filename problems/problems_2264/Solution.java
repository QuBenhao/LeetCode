package problems.problems_2264;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String largestGoodInteger(String num) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String num = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(largestGoodInteger(num));
    }
}
