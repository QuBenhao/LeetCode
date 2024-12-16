package problems.problems_3291;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minValidStrings(String[] words, String target) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] words = jsonArrayToStringArray(inputJsonValues[0]);
		String target = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(minValidStrings(words, target));
    }
}
