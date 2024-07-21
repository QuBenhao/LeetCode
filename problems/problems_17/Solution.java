package problems.problems_17;

import com.alibaba.fastjson.JSON;

import java.util.*;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final Map<Character, String> TRANSLATOR = new HashMap<>() {{
        put('2', "abc");
        put('3', "def");
        put('4', "ghi");
        put('5', "jkl");
        put('6', "mno");
        put('7', "pqrs");
        put('8', "tuv");
        put('9', "wxyz");
    }};

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits.isEmpty()) {
            return result;
        }
        dfs(0, digits, new StringBuilder(), result);
        return result;
    }

    private void dfs(int index, String digits, StringBuilder path, List<String> result) {
        if (index == digits.length()) {
            result.add(path.toString());
            return;
        }
        String letters = TRANSLATOR.get(digits.charAt(index));
        for (int i = 0; i < letters.length(); i++) {
            path.append(letters.charAt(i));
            dfs(index + 1, digits, path, result);
            path.deleteCharAt(path.length() - 1);
        }
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String digits = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(letterCombinations(digits));
    }
}
