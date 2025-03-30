package problems.problems_2278;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int percentageLetter(String s, char letter) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		char letter = inputJsonValues[1].length() > 1 ? inputJsonValues[1].charAt(1) : inputJsonValues[1].charAt(0);
        return JSON.toJSON(percentageLetter(s, letter));
    }
}
