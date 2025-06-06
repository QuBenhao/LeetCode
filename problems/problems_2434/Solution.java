package problems.problems_2434;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String robotWithString(String s) {
        int n = s.length();
        char[] suf = new char[n + 1];
        suf[n] = 'z';
        for (int i = n - 1; i >= 0; --i) {
            suf[i] = (char) Math.min(suf[i + 1], s.charAt(i));
        }
        StringBuilder ans = new StringBuilder();
        Stack<Character> st = new Stack<>();
        for (int i = 0; i < n; ++i) {
            char c = s.charAt(i);
            st.push(c);
            while (!st.isEmpty() && st.peek() <= suf[i+1]) {
                ans.append(st.pop());
            }
        }
        return ans.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(robotWithString(s));
    }
}
