package problems.problems_67;

import com.alibaba.fastjson.JSON;

import java.util.*;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String addBinary(String a, String b) {
        if (b.length() > a.length()) {
            String tmp = a;
            a = b;
            b = tmp;
        }
        StringBuilder sb = new StringBuilder(a.length() + 1);
        int cur = 0;
        for (int i = b.length() - 1; i >= 0; i--) {
            cur += a.charAt(i + a.length() - b.length()) - '0' + b.charAt(i) - '0';
            sb.append(cur % 2 == 0 ? '0' : '1');
            cur >>= 1;
        }
        for (int i = a.length() - b.length() - 1; i >= 0; i--) {
            cur += a.charAt(i) - '0';
            sb.append(cur % 2 == 0 ? '0' : '1');
            cur >>= 1;
        }
        if (cur > 0) {
            sb.append(cur % 2 == 0 ? '0' : '1');
        }
        return sb.reverse().toString();
    }

    @Override
    public Object solve(String[] values) {
        String a = jsonStringToString(values[0]);
        String b = jsonStringToString(values[1]);
        return JSON.toJSON(addBinary(a, b));
    }
}
