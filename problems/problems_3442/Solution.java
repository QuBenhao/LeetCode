package problems.problems_3442;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxDifference(String s) {
        int[] counts = new int[26];
        for (int i = 0; i < s.length(); ++i) {
            counts[s.charAt(i) - 'a']++;
        }
        int maxOdd = 0, minEven = s.length();
        for (int v: counts) {
            if (v == 0) {
                continue;
            }
            if (v % 2 == 1) {
                maxOdd = Math.max(maxOdd, v);
            } else {
                minEven = Math.min(minEven, v);
            }
        }
        return maxOdd - minEven;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(maxDifference(s));
    }
}
