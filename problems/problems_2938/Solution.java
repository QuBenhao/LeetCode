package problems.problems_2938;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minimumSteps(String s) {
        long ans = 0L, b = 0L;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                b++;
            } else {
                ans += b;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        String s = values[0];
        return JSON.toJSON(minimumSteps(s));
    }
}
