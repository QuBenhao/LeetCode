package problems.problems_242;

import com.alibaba.fastjson.JSON;

import java.util.*;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] counter = new int[26];
        for (int i = 0; i < s.length(); i++) {
            counter[s.charAt(i) - 'a']++;
            counter[t.charAt(i) - 'a']--;
        }
        return Arrays.stream(counter).allMatch(x -> x == 0);
    }

    @Override
    public Object solve(String[] values) {
        String s = jsonStringToString(values[0]);
        String t = jsonStringToString(values[1]);
        return JSON.toJSON(isAnagram(s, t));
    }
}
