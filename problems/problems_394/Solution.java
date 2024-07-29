package problems.problems_394;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String decodeString(String s) {
        Deque<String> stack = new ArrayDeque<>();
        Deque<Integer> numStack = new ArrayDeque<>();
        StringBuilder res = new StringBuilder();
        int multi = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '[') {
                numStack.push(multi);
                stack.push(res.toString());
                multi = 0;
                res = new StringBuilder();
            } else if (c == ']') {
                int t = numStack.pop();
                String last = stack.pop();
                StringBuilder tmp = new StringBuilder(last);
                for (int j = 0; j < t; j++) {
                    tmp.append(res);
                }
                res = tmp;
            } else if (c >= '0' && c <= '9') {
                multi = multi * 10 + Integer.parseInt(String.valueOf(c));
            } else {
                res.append(c);
            }
        }
        return res.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(decodeString(s));
    }
}
