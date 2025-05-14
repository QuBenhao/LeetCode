package problems.problems_2900;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<String> getLongestSubsequence(String[] words, int[] groups) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] words = jsonArrayToStringArray(inputJsonValues[0]);
		int[] groups = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(getLongestSubsequence(words, groups));
    }
}
