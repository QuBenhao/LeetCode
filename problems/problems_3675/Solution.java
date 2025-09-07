package problems.problems_3675;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minOperations(String s) {
        int cur = 26;
        for (int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) != 'a') {
                cur = Math.min(cur, s.charAt(i) - 'a');
            }
        }
        return 26 - cur;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(minOperations(s));
    }
}
