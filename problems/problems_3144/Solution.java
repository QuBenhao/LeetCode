package problems.problems_3144;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumSubstringsInPartition(String s) {
        int n = s.length();
        int[] dp = new int[n + 1];
        Arrays.fill(dp, n);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            int[] cnt = new int[26];
            int maxCnt = 0;
            int count = 0;
            for (int j = i; j >= 0; j--) {
                int c = s.charAt(j) - 'a';
                if (cnt[c]++ == 0) {
                    count++;
                }
                maxCnt = Math.max(maxCnt, cnt[c]);
                if (i - j + 1 == maxCnt * count) {
                    dp[i + 1] = Math.min(dp[i + 1], dp[j] + 1);
                }
            }
        }
        return dp[n];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(minimumSubstringsInPartition(s));
    }
}
