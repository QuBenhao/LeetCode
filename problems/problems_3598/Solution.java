package problems.problems_3598;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {

    private int getPrefixLength(String[] words, int i, int j) {
        int k = 0;
        while (k < words[i].length() && k < words[j].length() && words[i].charAt(k) == words[j].charAt(k)) { ++k; }
        return k;
    }

    public int[] longestCommonPrefix(String[] words) {
        int n = words.length;
        if (n == 1) {
            return new int[]{0};
        }
        int[] pls = new int[n];
        int[] suffix = new int[n];
        for (int i = 1; i < n; ++i) {
            pls[i] = getPrefixLength(words, i - 1, i);
        }
        for (int i = n - 2; i >= 0; --i) {
            suffix[i] = Math.max(suffix[i + 1], pls[i + 1]);
        }
        int[] ans = new int[n];
        ans[0] = suffix[1];
        int pre = 0;
        for (int i = 1; i < n - 1; ++i) {
            ans[i] = Math.max(Math.max(pre, suffix[i + 1]), getPrefixLength(words, i -1, i + 1));
            pre = Math.max(pre, pls[i]);
        }
        ans[n - 1] = pre;
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] words = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(longestCommonPrefix(words));
    }
}
