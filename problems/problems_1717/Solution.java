package problems.problems_1717;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    @FunctionalInterface
    interface BooleanOperation {
        boolean apply(int i);
    }

    public int maximumGain(String s, int x, int y) {
        BooleanOperation isA;
        BooleanOperation isB;
        if (x < y) {
            isA = (i) -> s.charAt(i) == 'b';
            isB = (i) -> s.charAt(i) == 'a';
            int temp = x;
            x = y;
            y = temp;
        } else {
            isA = (i) -> s.charAt(i) == 'a';
            isB = (i) -> s.charAt(i) == 'b';
        }
        int n = s.length();
        int ans = 0;
        int i = 0;
        while (i < n) {
            while (i < n && !isA.apply(i) && !isB.apply(i)) {
                ++i;
            }
            int ca = 0, cb = 0;
            while (i < n && (isA.apply(i) || isB.apply(i))) {
                if (isA.apply(i)) {
                    ++ca;
                } else {
                    if (ca > 0) {
                        ans += x;
                        --ca;
                    } else {
                        ++cb;
                    }
                }
                ++i;
            }
            ans += Math.min(ca, cb) * y;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		int x = Integer.parseInt(inputJsonValues[1]);
		int y = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maximumGain(s, x, y));
    }
}
