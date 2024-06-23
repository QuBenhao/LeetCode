package problems.problems_520;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean detectCapitalUse(String word) {
        if (Character.isUpperCase(word.charAt(word.length() - 1))) {
            for (int i = 0; i < word.length() - 1; i++) {
                if (Character.isLowerCase(word.charAt(i))) {
                    return false;
                }
            }
        } else if (Character.isUpperCase(0)) {
            for (int i = 1; i < word.length() - 1; i++) {
                if (Character.isUpperCase(word.charAt(i))) {
                    return false;
                }
            }
        } else {
            for (int i = 1; i < word.length() - 1; i++) {
                if (Character.isUpperCase(word.charAt(i))) {
                    return false;
                }
            }
        }
        return true;
    }

    @Override
    public Object solve(String[] values) {
        String word = jsonStringToString(values[0]);
        return JSON.toJSON(detectCapitalUse(word));
    }
}
