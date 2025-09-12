package problems.problems_3541;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final String VOWELS = "aeiou";

    public int maxFreqSum(String s) {
        int[] vowelsCount = new int[5], nonVowesCount = new int[26];
        for (char c: s.toCharArray()) {
            int idx = VOWELS.indexOf(c);
            if (idx != -1) {
                ++vowelsCount[idx];
            } else {
                ++nonVowesCount[c - 'a'];
            }
        }
        return arrayMax(vowelsCount) + arrayMax(nonVowesCount);
    }

    private int arrayMax(int[] arr) {
        int ans = 0;
        for (int v: arr) {
            ans = Math.max(ans, v);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(maxFreqSum(s));
    }
}
