package problems.problems_3227;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private  static final String VOWELS = "aeiou";
    public boolean doesAliceWin(String s) {
        for (int i = 0; i < s.length(); ++i) {
            if (VOWELS.indexOf(s.charAt(i)) >= 0) {
                return true;
            }
        }
        return false;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(doesAliceWin(s));
    }
}
