package problems.problems_13;

import com.alibaba.fastjson.JSON;

import java.util.*;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int romanToInt(String s) {
        Map<Character, Integer> romanMap = new HashMap<>() {{
            put('I', 1);
            put('V', 5);
            put('X', 10);
            put('L', 50);
            put('C', 100);
            put('D', 500);
            put('M', 1000);
        }};
        int ans = romanMap.get(s.charAt(0)), last = ans;
        for (int i = 1; i < s.length(); i++) {
            int v = romanMap.get(s.charAt(i));
            ans += v;
            if (last < v) {
                ans -= last << 1;
            }
            last = v;
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        String s = jsonStringToString(values[0]);
        return JSON.toJSON(romanToInt(s));
    }
}
