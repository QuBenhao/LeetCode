package problems.problems_LCR_094;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minCut(String s) {
        int n = s.length();
        if (n < 2) {
            return 0;
        }
        boolean[][] g = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            g[i][i] = true;
            for (int j = 0; j < i; j++) {
                g[j][i] = s.charAt(j) == s.charAt(i) && (i - j < 2 || g[j + 1][i - 1]);
            }
        }
        int[] f = new int[n];
        Arrays.fill(f, Integer.MAX_VALUE / 2);
        for (int i = 0; i < n; i++) {
            if (g[0][i]) {
                f[i] = 0;
            } else {
                for (int j = 0; j < i; j++) {
                    if (g[j + 1][i]) {
                        f[i] = Math.min(f[i], f[j] + 1);
                    }
                }
            }
        }
        return f[n - 1];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(minCut(s));
    }
}
