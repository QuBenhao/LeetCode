package problems.problems_3136;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final String VOWELS = "aeiou";
    public boolean isValid(String word) {
        if (word.length() < 3) {
            return false;
        }
        boolean hasVowel = false, hasConsonant = false;
        for (char c : word.toCharArray()) {
            if (Character.isLetter(c)) {
                char lowerC = Character.toLowerCase(c);
                if (VOWELS.indexOf(lowerC) >= 0) {
                    hasVowel = true;
                } else if (!hasConsonant) {
                    hasConsonant = true;
                }
            } else if (!Character.isDigit(c)) {
                return false; // Invalid character
            }
        }
        return hasVowel && hasConsonant;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String word = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(isValid(word));
    }
}
