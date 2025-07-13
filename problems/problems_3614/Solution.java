package problems.problems_3614;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public char processStr(String s, long k) {
        long length = 0L;
        int n = s.length();
        Set<Integer> invalids = new HashSet<>();
        for (int i = 0; i < n; ++i) {
            char c = s.charAt(i);
            if (c == '#') {
                length *= 2;
            } else if (c == '*') {
                if (length > 0) {
                    length--;
                } else {
                    invalids.add(i);
                }
            } else if (c != '%') {
                length++;
            }
        }
        if (k >= length) {
            return '.';
        }
        for (int i = n - 1; i >= 0; --i) {
            if (invalids.contains(i)) continue;
            char c = s.charAt(i);
            switch (c) {
                case '#':
                    length /= 2;
                    k %= length;
                    break;
                case '%':
                    k = length - 1 - k;
                    break;
                case '*':
                    ++length;
                    break;
                default:
                    if (k == length - 1) {
                        return c;
                    }
                    --length;
            }
        }
        return '.';
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		long k = Long.parseLong(inputJsonValues[1]);
        return JSON.toJSON(processStr(s, k));
    }
}
