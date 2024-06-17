package problems.problems_522;

import com.alibaba.fastjson.JSON;

import java.util.*;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private boolean isSubSeq(String s, String t) {
        int ptr_s = 0;
        for (int ptr_t = 0; ptr_t < t.length() && ptr_s < s.length(); ptr_t++) {
            if (s.charAt(ptr_s) == t.charAt(ptr_t)) {
                ptr_s++;
            }
        }
        return ptr_s == s.length();
    }

    public int findLUSlength(String[] strs) {
        int ans = -1;
        out:
        for (int i = 0; i < strs.length; i++) {
            if (strs[i].length() > ans) {
                for (int j = 0; j < strs.length; j++) {
                    if (j != i && isSubSeq(strs[i], strs[j])) {
                        continue out;
                    }
                }
                ans = strs[i].length();
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        String[] strs = jsonArrayToStringArray(values[0]);
        return JSON.toJSON(findLUSlength(strs));
    }
}
