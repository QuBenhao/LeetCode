package problems.problems_3612;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String processStr(String s) {
        StringBuilder sb = new StringBuilder();
        for (char c: s.toCharArray()) {
            switch (c) {
                case '#':
                    sb.append(sb);
                    break;
                case '%':
                    sb.reverse();
                    break;
                case '*':
                    if (!sb.isEmpty()) {
                        sb.deleteCharAt(sb.length() - 1);
                    }
                    break;
                default:
                    sb.append(c);
            }
        }
        return sb.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(processStr(s));
    }
}
