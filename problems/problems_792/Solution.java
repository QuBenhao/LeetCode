package problems.problems_792;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numMatchingSubseq(String s, String[] words) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		String[] words = jsonArrayToStringArray(inputJsonValues[1]);
        return JSON.toJSON(numMatchingSubseq(s, words));
    }
}
