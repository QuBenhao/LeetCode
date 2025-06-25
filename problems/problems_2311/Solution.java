package problems.problems_2311;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int longestSubsequence(String s, int k) {
        int ans = 0;
        int n = s.length(), cur = 0;
        for (int i = n - 1; i >= 0; --i) {
            if (s.charAt(i) == '0') {
                ++ans;
            } else if (n - 1 - i < 31) {
                int bit = 1 << (n - 1 - i);
                if (cur + bit <= k) {
                    cur += bit;
                    ++ans;
                }
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(longestSubsequence(s, k));
    }
}
