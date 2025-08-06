package problems.problems_3363;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxCollectedFruits(int[][] fruits) {
        int n = fruits.length;
        int ans = fruits[0][0] + fruits[n - 1][n - 1];
        int[] dp1 = new int[n + 1];
        int[] dp2 = new int[n + 1];
        dp1[n - 1] = fruits[0][n - 1];
        dp2[n - 1] = fruits[n - 1][0];
        for (int i = 1; i < n - 1; ++i) {
            ans += fruits[i][i];
            int[] nextDp1 = new int[n + 1];
            int[] nextDp2 = new int[n + 1];
            for (int j = Math.max(n - 1 - i, i + 1); j < n; ++j) {
                nextDp1[j] = Math.max(Math.max(dp1[j - 1], dp1[j]), dp1[j + 1]) + fruits[i][j];
                nextDp2[j] = Math.max(Math.max(dp2[j - 1], dp2[j]), dp2[j + 1]) + fruits[j][i];
            }
            dp1 = nextDp1;
            dp2 = nextDp2;
        }
        return ans + dp1[n - 1] + dp2[n - 1];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] fruits = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(maxCollectedFruits(fruits));
    }
}
