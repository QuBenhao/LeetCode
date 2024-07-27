package problems.problems_3106;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int distance(char a, char b) {
        return Math.min((a - b + 26) % 26, (b - a + 26) % 26);
    }
    public String getSmallestString(String s, int k) {
        StringBuilder sb = new StringBuilder();
        int idx = 0;
        while (idx < s.length() && k > 0) {
            if (s.charAt(idx) == 'a') {
                sb.append('a');
            } else {
                int d = distance('a', s.charAt(idx));
                if (d <= k) {
                    sb.append('a');
                    k -= d;
                } else {
                    sb.append((char) (s.charAt(idx) - k));
                    k = 0;
                }
            }
            idx++;
        }
        sb.append(s.substring(idx));
        return sb.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(getSmallestString(s, k));
    }
}
