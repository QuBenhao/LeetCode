package problems.problems_2414;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int longestContinuousSubstring(String s) {
        int ans = 1, n = s.length();
        for (int i = 0, cur = 1; i < n - 1; i++) {
            if (s.charAt(i + 1) - s.charAt(i) == 1) {
                cur++;
                ans = Math.max(ans, cur);
            } else {
                cur = 1;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(longestContinuousSubstring(s));
    }
}
