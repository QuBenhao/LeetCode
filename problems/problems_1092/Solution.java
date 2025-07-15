package problems.problems_1092;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String shortestCommonSupersequence(String str1, String str2) {
        int m = str1.length(), n = str2.length();
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (str1.charAt(i) == str2.charAt(j)) {
                    dp[i + 1][j + 1] = dp[i][j] + 1;
                } else {
                    dp[i + 1][j + 1] = Math.max(dp[i + 1][j], dp[i][j + 1]);
                }
            }
        }
        StringBuilder result = new StringBuilder();
        for (int i = m - 1, j = n - 1; i >= 0 || j >= 0;) {
            if (i < 0) {
                result.append(str2.charAt(j--));
                continue;
            }
            if (j < 0) {
                result.append(str1.charAt(i--));
                continue;
            }
            if (str1.charAt(i) == str2.charAt(j)) {
                result.append(str1.charAt(i));
                --i;
                --j;
            } else if (dp[i + 1][j] <= dp[i][j + 1]) {
                result.append(str1.charAt(i--));
            } else {
                result.append(str2.charAt(j--));
            }
        }
        return result.reverse().toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String str1 = jsonStringToString(inputJsonValues[0]);
		String str2 = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(shortestCommonSupersequence(str1, str2));
    }
}
