package problems.problems_600;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findIntegers(int n) {
        int[] dp = new int[31];
        dp[0] = 1;
        dp[1] = 2;
        for (int i = 2; i < 31; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        n++;
        int ans = 0, pre = 0;
        for (int i = 29; i >= 0; i--) {
            if ((n & (1 << i)) > 0) {
                ans += dp[i];
                if (pre == 1) {
                    break;
                }
                pre = 1;
            } else {
                pre = 0;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(findIntegers(n));
    }
}
