package problems.problems_2555;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximizeWin(int[] prizePositions, int k) {
        int ans = 0;
        int n = prizePositions.length;
        int[] dp = new int[n + 1];
        for (int left = 0, right = 0; right < n; right++) {
            while (prizePositions[right] - prizePositions[left] > k) {
                left++;
            }
            dp[right + 1] = Math.max(dp[right], right - left + 1);
            ans = Math.max(ans, dp[left] + right - left + 1);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] prizePositions = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maximizeWin(prizePositions, k));
    }
}
