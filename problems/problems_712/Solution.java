package problems.problems_712;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumDeleteSum(String s1, String s2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s1 = jsonStringToString(inputJsonValues[0]);
		String s2 = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(minimumDeleteSum(s1, s2));
    }
}
