package problems.problems_2785;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;

public class Solution extends BaseSolution {
    private static final String VOwELS = "AEIOUaeiou";

    public String sortVowels(String s) {
        StringBuilder sb = new StringBuilder();
        char[] chars = s.toCharArray();
        for (char c : chars) {
            if (VOwELS.indexOf(c) >= 0) {
                sb.append(c);
            }
        }

        char[] vowels = sb.toString().toCharArray();
        Arrays.sort(vowels);

        for (int i = 0, j = 0; i < chars.length && j < vowels.length; ++i) {
            if (VOwELS.indexOf(chars[i]) >= 0) {
                chars[i] = vowels[j++];
            }
        }
        return new String(chars);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(sortVowels(s));
    }
}
