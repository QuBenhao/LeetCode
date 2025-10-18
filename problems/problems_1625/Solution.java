package problems.problems_1625;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String findLexSmallestString(String s, int a, int b) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		int a = Integer.parseInt(inputJsonValues[1]);
		int b = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(findLexSmallestString(s, a, b));
    }
}
