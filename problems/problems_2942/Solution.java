package problems.problems_2942;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] words = jsonArrayToStringArray(inputJsonValues[0]);
		char x = inputJsonValues[1].length() > 1 ? inputJsonValues[1].charAt(1) : inputJsonValues[1].charAt(0);
        return JSON.toJSON(findWordsContaining(words, x));
    }
}
