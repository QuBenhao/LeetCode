package problems.problems_316;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String removeDuplicateLetters(String s) {
        int[] lastIndex = new int[26];
        boolean[] seen = new boolean[26];
        List<Character> stack = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            lastIndex[s.charAt(i) - 'a'] = i;
        }
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (seen[c - 'a']) {
                continue;
            }
            while (!stack.isEmpty() && stack.get(stack.size() - 1) > c &&
                   lastIndex[stack.get(stack.size() - 1) - 'a'] > i) {
                seen[stack.get(stack.size() - 1) - 'a'] = false;
                stack.remove(stack.size() - 1);
            }
            stack.add(c);
            seen[c - 'a'] = true;
        }
        StringBuilder result = new StringBuilder();
        for (char c : stack) {
            result.append(c);
        }
        return result.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(removeDuplicateLetters(s));
    }
}
