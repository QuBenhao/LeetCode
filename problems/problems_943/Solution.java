package problems.problems_943;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int getMax(int[][] dp, int n, int st) {
        int idx = -1, m = -1;
        for (int i = 0; i < n; ++i) {
            if (((st >> i) & 1) == 1 && dp[st][i] > m) {
                m = dp[st][i];
                idx = i;
            }
        }
        return idx;
    }
    public String shortestSuperstring(String[] words) {
        int n = words.length;
        int[][] g = new int[n][n];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i != j) {
                    for (int k = Math.min(words[i].length(), words[j].length()); k > 0; --k) {
                        if (words[i].endsWith(words[j].substring(0, k))) {
                            g[i][j] = k;
                            break;
                        }
                    }
                }
            }
        }
        int mask = 1 << n;
        int[][] dp = new int[mask][n];
        int[][] track = new int[mask][n];
        for (int i = 0; i < mask; i++) {
            Arrays.fill(track[i], -1);
        }
        for (int s = 1; s < mask; ++s) {
            for (int i = 0; i < n; ++i) {
                if (((s >> i) & 1) == 0) continue;
                for (int j = 0; j < n; ++j) {
                    if (i == j || ((s >> j) & 1) == 1) continue;
                    int next = s | (1 << j);
                    int len = dp[s][i] + g[i][j];
                    if (len > dp[next][j]) {
                        dp[next][j] = len;
                        track[next][j] = i;
                    }
                }
            }
        }
        int st = mask - 1;
        int idx = getMax(dp, n, st);
        String ans = words[idx];
        while (st > 0) {
            int prev = track[st][idx];
            st ^= 1 << idx;
            if (prev == -1) {
                idx = getMax(dp, n, st);
                if (idx != -1) {
                    ans = words[idx] + ans;
                }
            } else {
                ans = words[prev].substring(0, words[prev].length() - g[prev][idx]) + ans;
                idx = prev;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] words = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(shortestSuperstring(words));
    }
}
