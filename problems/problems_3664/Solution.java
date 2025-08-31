package problems.problems_3664;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int score(String[] cards, char x) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] cards = jsonArrayToStringArray(inputJsonValues[0]);
		char x = inputJsonValues[1].length() > 1 ? inputJsonValues[1].charAt(1) : inputJsonValues[1].charAt(0);
        return JSON.toJSON(score(cards, x));
    }
}
