package problems.problems_3333;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int MOD = 1_000_000_007;

    public int possibleStringCount(String word, int k) {
        int n = word.length();
        long ans = 1L;
        List<Integer> groups = new ArrayList<>();
        for (int i = 0; i < n; ) {
            char c = word.charAt(i);
            int start = i;
            while (i < n && word.charAt(i) == c) {
                ++i;
            }
            --k;
            int cur = i - start;
            if (cur > 1) {
                ans = (ans * cur) % MOD;
                groups.add(cur - 1);
            }
        }
        if (k <= 0) {
            return (int) ans;
        }
        int[] dp = new int[k];
        Arrays.fill(dp, 1);
        for (int g: groups) {
            for (int i = 1; i < k; ++i) {
                dp[i] = (dp[i] + dp[i - 1]) % MOD;
            }
            for (int i = k - 1; i > g; --i) {
                dp[i] = (dp[i] - dp[i - g - 1] + MOD) % MOD;
            }
        }
        return (int) (ans - dp[k - 1] + MOD) % MOD;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String word = jsonStringToString(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(possibleStringCount(word, k));
    }
}
