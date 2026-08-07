package problems.problems_3302;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] validSequence(String word1, String word2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String word1 = jsonStringToString(inputJsonValues[0]);
		String word2 = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(validSequence(word1, word2));
    }
}
