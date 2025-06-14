package problems.problems_1432;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxDiff(int num) {
        String s = String.valueOf(num);
        int n = s.length();
        int max, min;
        int idx = 0;
        while (idx < n && s.charAt(idx) == '9') {
            idx++;
        }
        if (idx == n) {
            max = num;
        } else {
            max = Integer.parseInt(s.replace(s.charAt(idx), '9'));
        }
        if (s.charAt(0) == '1') {
            idx = 1;
            while (idx < n && (s.charAt(idx) == '0' || s.charAt(idx) == '1')) {
                idx++;
            }
            if (idx == n) {
                min = num;
            } else {
                min = Integer.parseInt(s.replace(s.charAt(idx), '0'));
            }
        } else {
            min = Integer.parseInt(s.replace(s.charAt(0), '1'));
        }
        return max - min;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int num = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(maxDiff(num));
    }
}
