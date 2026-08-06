package problems.problems_3348;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String smallestNumber(String num, long t) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String num = jsonStringToString(inputJsonValues[0]);
		long t = Long.parseLong(inputJsonValues[1]);
        return JSON.toJSON(smallestNumber(num, t));
    }
}
