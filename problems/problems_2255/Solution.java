package problems.problems_2255;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countPrefixes(String[] words, String s) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] words = jsonArrayToStringArray(inputJsonValues[0]);
		String s = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(countPrefixes(words, s));
    }
}
