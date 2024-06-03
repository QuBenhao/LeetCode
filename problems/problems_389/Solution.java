package problems.problems_389;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public char findTheDifference(String s, String t) {
        int[] counter = new int[26];
        for (int i = 0; i < s.length(); i++) {
            counter[s.charAt(i) - 'a']--;
            counter[t.charAt(i) - 'a']++;
        }
        counter[t.charAt(t.length() - 1) - 'a']++;
        for (int i = 0; i < 26; i++) {
            if (counter[i] > 0) {
                return (char)('a' + i);
            }
        }
        return 'a';
    }

    @Override
    public Object solve(String[] values) {
        String s = values[0];
		String t = values[1];
        return JSON.toJSON(findTheDifference(s, t));
    }
}
