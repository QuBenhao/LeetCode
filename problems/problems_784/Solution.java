package problems.problems_784;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private void dfs(List<String> result, StringBuilder current, String s, int index) {
        if (index == s.length()) {
            result.add(current.toString());
            return;
        }
        
        char c = s.charAt(index);
        current.append(c);
        dfs(result, current, s, index + 1);
        current.deleteCharAt(current.length() - 1);
        
        if (Character.isLetter(c)) {
            current.append((char)(c ^ 32)); // Toggle case using bitwise XOR
            dfs(result, current, s, index + 1);
            current.deleteCharAt(current.length() - 1);
        }
    }
    
    public List<String> letterCasePermutation(String s) {
        List<String> result = new ArrayList<>();
        StringBuilder current = new StringBuilder();
        dfs(result, current, s, 0);
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(letterCasePermutation(s));
    }
}
