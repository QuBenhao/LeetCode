package problems.problems_3216;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String getSmallestString(String s) {
        int n = s.length();
        char[] ch = s.toCharArray();
        for (int i = 0; i < n - 1; i++) {
            if (ch[i] > ch[i + 1] && ch[i] % 2 == ch[i + 1] % 2) {
                char c = ch[i];
                ch[i] = ch[i + 1];
                ch[i + 1] = c;
                return new String(ch);
            }
        }
        return s;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(getSmallestString(s));
    }
}
