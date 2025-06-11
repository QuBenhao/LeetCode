package problems.problems_2767;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private boolean isFivePow(int n) {
        if (n == 0) return false;
        while (n % 5 == 0) {
            n /= 5;
        }
        return n == 1;
    }
    public int minimumBeautifulSubstrings(String s) {
        int n = s.length();
        int[] preSum = new int[n + 1];
        for (int i = 0; i < n; ++i) {
            preSum[i+1] = (preSum[i] << 1) + (s.charAt(i) - '0');
        }
        int[] dp = new int[n + 1];
        Arrays.fill(dp, n + 1);
        dp[0] = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j <= i; ++j) {
                if (s.charAt(j) == '0') continue;
                int num = preSum[i + 1] ^ (preSum[j] << (i - j + 1));
                if (isFivePow(num)) {
                    dp[i + 1] = Math.min(dp[i + 1], dp[j] + 1);
                }
            }
        }
        return dp[n] == n + 1 ? -1 : dp[n];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(minimumBeautifulSubstrings(s));
    }
}
