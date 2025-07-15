package problems.problems_3201;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumLength(int[] nums) {
        int ans = 0;
        int[] dp = new int[4];
        for (int num: nums) {
            int cur = num & 1;
            for (int i = 0; i < 4; ++i) {
                if (((i >> (dp[i] & 1)) & 1) == cur) {
                    ans = Math.max(ans, ++dp[i]);
                }
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maximumLength(nums));
    }
}
