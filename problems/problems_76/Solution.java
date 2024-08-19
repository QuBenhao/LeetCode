package problems.problems_76;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String minWindow(String s, String t) {
        int[] cntS = new int[52], cntT = new int[52];
        int diff = 0;
        for (char c : t.toCharArray()) {
            int idx = getCharIdx(c);
            if (cntT[idx]++ == 0) {
                diff++;
            }
        }
        int ans_left = -1, ans_right = -1;
        for (int left = 0, right = 0; right < s.length(); right++) {
            int idx = getCharIdx(s.charAt(right));
            if (++cntS[idx] == cntT[idx]) {
                diff--;
            }
            while (left < right) {
                int idxLeft = getCharIdx(s.charAt(left));
                if (cntS[idxLeft] > cntT[idxLeft] && --cntS[idxLeft] >= 0) {
                    left++;
                } else {
                    break;
                }
            }
            if (diff == 0 && (ans_left == -1 || right - left < ans_right - ans_left)) {
                ans_left = left;
                ans_right = right;
            }
        }
        return ans_left == -1 ? "" : s.substring(ans_left, ans_right + 1);
    }

    private int getCharIdx(char c) {
        return c >= 'A' && c <= 'Z' ? c - 'A' : c - 'a' + 26;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		String t = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(minWindow(s, t));
    }
}
