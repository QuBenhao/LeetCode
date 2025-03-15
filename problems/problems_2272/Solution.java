package problems.problems_2272;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int largestVariance(String s) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(largestVariance(s));
    }
}
