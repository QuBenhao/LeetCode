package problems.problems_2734;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String smallestString(String s) {
        StringBuilder sb = new StringBuilder();
        int n = s.length();
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) != 'a') {
                sb.append(s.substring(0, i));
                for (; i < n && s.charAt(i) != 'a'; i++) {
                    sb.append((char)(s.charAt(i) - 1));
                }
                sb.append(s.substring(i));
                return sb.toString();
            }
        }
        return s.substring(0, n - 1) + 'z';
    }

    @Override
    public Object solve(String[] values) {
        String s = jsonStringToString(values[0]);
        return JSON.toJSON(smallestString(s));
    }
}
