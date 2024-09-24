package problems.problems_LCR_017;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String minWindow(String s, String t) {
        int ansLeft = -1, ansRight = -1;
        int left = 0, right = 0;
        Map<Character, Integer> counter = new HashMap<>();
        for (int i = 0; i < t.length(); i++) {
            counter.put(t.charAt(i), counter.getOrDefault(t.charAt(i), 0) + 1);
        }
        int diff = counter.size();
        while (right < s.length()) {
            char c = s.charAt(right);
            if (counter.containsKey(c)) {
                counter.put(c, counter.get(c) - 1);
                if (counter.get(c) == 0) {
                    diff--;
                }
            }
            right++;
            while (diff == 0) {
                if (ansLeft == -1 || right - left < ansRight - ansLeft) {
                    ansLeft = left;
                    ansRight = right;
                }
                char c1 = s.charAt(left);
                if (counter.containsKey(c1)) {
                    counter.put(c1, counter.get(c1) + 1);
                    if (counter.get(c1) == 1) {
                        diff++;
                    }
                }
                left++;
            }
        }
        return ansLeft == -1 ? "" : s.substring(ansLeft, ansRight);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		String t = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(minWindow(s, t));
    }
}
