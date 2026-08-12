package problems.problems_2213;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] longestRepeating(String s, String queryCharacters, int[] queryIndices) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		String queryCharacters = jsonStringToString(inputJsonValues[1]);
		int[] queryIndices = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(longestRepeating(s, queryCharacters, queryIndices));
    }
}
