package problems.problems_3332;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxScore(int n, int k, int[][] stayScore, int[][] travelScore) {
        int[][] dp = new int[2][n];
        for (int i = 0; i < k; ++i) {
            int cur = i % 2, nxt = cur ^ 1;
            for (int j = 0; j < n; ++j) {
                for (int jj = 0; jj < n; ++jj) {
                    if (j == jj) {
                        dp[nxt][j] = Math.max(dp[nxt][j], dp[cur][j] + stayScore[i][j]);
                    } else {
                        dp[nxt][jj] = Math.max(dp[nxt][jj], dp[cur][j] + travelScore[j][jj]);
                    }
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = Math.max(ans, dp[k % 2][i]);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int[][] stayScore = jsonArrayToInt2DArray(inputJsonValues[2]);
		int[][] travelScore = jsonArrayToInt2DArray(inputJsonValues[3]);
        return JSON.toJSON(maxScore(n, k, stayScore, travelScore));
    }
}
