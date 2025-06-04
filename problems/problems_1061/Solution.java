package problems.problems_1061;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String smallestEquivalentString(String s1, String s2, String baseStr) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s1 = jsonStringToString(inputJsonValues[0]);
		String s2 = jsonStringToString(inputJsonValues[1]);
		String baseStr = jsonStringToString(inputJsonValues[2]);
        return JSON.toJSON(smallestEquivalentString(s1, s2, baseStr));
    }
}
