package problems.problems_20;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        String left = "([{", right = ")]}";
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (left.indexOf(c) != -1) {
                stack.push(c);
            } else if (stack.isEmpty() || stack.pop() != left.charAt(right.indexOf(c))) {
                return false;
            }
        }
        return stack.isEmpty();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(isValid(s));
    }
}
