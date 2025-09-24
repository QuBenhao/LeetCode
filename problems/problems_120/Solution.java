package problems.problems_120;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n = triangle.size();
        int[] dp = new int[n];
        dp[0] = triangle.get(0).get(0);
        for (int i = 1; i < n; ++i) {
            var cur = triangle.get(i);
            dp[i] = cur.getLast() + dp[i - 1];
            for (int j = i - 1; j > 0; --j) {
                dp[j] = Math.min(dp[j - 1], dp[j]) + cur.get(j);
            }
            dp[0] += cur.getFirst();
        }
        int ans = dp[0];
        for (int i = 1; i < n; ++i) {
            ans = Math.min(ans, dp[i]);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<List<Integer>> triangle = jsonArrayTo2DIntList(inputJsonValues[0]);
        return JSON.toJSON(minimumTotal(triangle));
    }
}
