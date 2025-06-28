package problems.problems_1678;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String interpret(String command) {
        StringBuilder result = new StringBuilder();
        int n = command.length();
        for (int i = 0; i < n; i++) {
            if (command.charAt(i) == 'G') {
                result.append('G');
            } else if (command.charAt(i) == '(') {
                if (i + 1 < n && command.charAt(i + 1) == ')') {
                    result.append('o');
                    i++; // Skip the next character
                } else {
                    result.append("al");
                    i += 3; // Skip "al)"
                }
            }
        }
        return result.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String command = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(interpret(command));
    }
}
