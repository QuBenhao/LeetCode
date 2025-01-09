package problems.problems_3298;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long validSubstringCount(String word1, String word2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String word1 = jsonStringToString(inputJsonValues[0]);
		String word2 = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(validSubstringCount(word1, word2));
    }
}
