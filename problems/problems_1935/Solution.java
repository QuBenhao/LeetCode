package problems.problems_1935;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int canBeTypedWords(String text, String brokenLetters) {
        int brokenMask = 0;
        for (char c : brokenLetters.toCharArray()) {
            brokenMask |= 1 << (c - 'a'); // Add c to the set
        }

        int ans = 0;
        int ok = 1;
        for (char c : text.toCharArray()) {
            if (c == ' ') { // Finished traversing the previous word
                ans += ok;
                ok = 1;
            } else if ((brokenMask >> (c - 'a') & 1) > 0) { // c is in brokenLetters
                ok = 0;
            }
        }
        ans += ok; // Last word
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String text = jsonStringToString(inputJsonValues[0]);
		String brokenLetters = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(canBeTypedWords(text, brokenLetters));
    }
}
