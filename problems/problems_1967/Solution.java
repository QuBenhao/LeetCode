package problems.problems_1967;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numOfStrings(String[] patterns, String word) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] patterns = jsonArrayToStringArray(inputJsonValues[0]);
		String word = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(numOfStrings(patterns, word));
    }
}
