package problems.problems_744;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public char nextGreatestLetter(char[] letters, char target) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[] letters = jsonArrayToCharArray(inputJsonValues[0]);
		char target = inputJsonValues[1].length() > 1 ? inputJsonValues[1].charAt(1) : inputJsonValues[1].charAt(0);
        return JSON.toJSON(nextGreatestLetter(letters, target));
    }
}
