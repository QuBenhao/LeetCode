package problems.problems_3628;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long numOfSubsequences(String s) {
        int n = s.length();
        int[] sufT = new int[n + 1];
        int[] sufC = new int[n + 1];
        for (int i = n - 1; i >= 0; --i) {
            sufT[i] = sufT[i + 1] + (s.charAt(i) == 'T' ? 1 : 0);
            sufC[i] = sufC[i + 1] + (s.charAt(i) == 'C' ? sufT[i] : 0);
        }
        long ans = 0, maxAdd = 0;
        int preL = 0, preC = 0;
        for (int i = 0; i < n; ++i) {
            char c = s.charAt(i);
            if (c == 'L') {
                ++preL;
                ans += sufC[i];
            } else if (c == 'C') {
                preC += preL;
            }
            maxAdd = Math.max(maxAdd, Math.max(Math.max(preC, sufC[i]), (long) preL * sufT[i]));
        }
        return ans + maxAdd;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(numOfSubsequences(s));
    }
}
