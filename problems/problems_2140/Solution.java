package problems.problems_2140;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long mostPoints(int[][] questions) {
        int n = questions.length;
        long[] dp = new long[n + 1];
        for (int i = 0; i < n; i++) {
            dp[i + 1] = Math.max(dp[i + 1], dp[i]);
            int next = Math.min(n, i + questions[i][1] + 1);
            dp[next] = Math.max(dp[next], dp[i] + questions[i][0]);
        }
        return dp[n];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] questions = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(mostPoints(questions));
    }
}
