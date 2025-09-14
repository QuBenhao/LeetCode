package problems.problems_1935;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int canBeTypedWords(String text, String brokenLetters) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String text = jsonStringToString(inputJsonValues[0]);
		String brokenLetters = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(canBeTypedWords(text, brokenLetters));
    }
}
