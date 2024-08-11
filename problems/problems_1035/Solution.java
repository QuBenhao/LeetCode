package problems.problems_1035;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxUncrossedLines(int[] nums1, int[] nums2) {
        int m = nums1.length, n = nums2.length;
        int[][] dp = new int[m + 1][n + 1];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (nums1[i] == nums2[j]) {
                    dp[i + 1][j + 1] = dp[i][j] + 1;
                } else {
                    dp[i + 1][j + 1] = Math.max(dp[i + 1][j], dp[i][j + 1]);
                }
            }
        }
        return dp[m][n];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] nums2 = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(maxUncrossedLines(nums1, nums2));
    }
}
