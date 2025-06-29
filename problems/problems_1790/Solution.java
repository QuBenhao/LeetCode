package problems.problems_1790;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean areAlmostEqual(String s1, String s2) {
        int d1 = -1, d2 = -1;
        for (int i = 0; i < s1.length(); ++i) {
            if (s1.charAt(i) != s2.charAt(i)) {
                if (d1 == -1) {
                    d1 = i;
                } else if (d2 == -1) {
                    d2 = i;
                } else {
                    return false;
                }
            }
        }
        if (d1 == -1) {
            return true;
        }
        if (d2 == -1) {
            return false;
        }
        return s1.charAt(d1) == s2.charAt(d2) && s1.charAt(d2) == s2.charAt(d1);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s1 = jsonStringToString(inputJsonValues[0]);
		String s2 = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(areAlmostEqual(s1, s2));
    }
}
