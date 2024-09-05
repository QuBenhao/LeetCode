package problems.problems_LCR_092;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minFlipsMonoIncr(String s) {
        int n = s.length();
        int ans = n, one = 0;
        for (int i = 0; i < n; i++) {
            ans = Math.min(ans, one * 2 - i);
            one += s.charAt(i) - '0';
        }
        return Math.min(ans + n - one, one);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(minFlipsMonoIncr(s));
    }
}
