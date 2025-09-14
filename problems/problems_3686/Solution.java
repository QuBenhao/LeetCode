package problems.problems_3686;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int MOD = (int)1e9 + 7;
    public int countStableSubsequences(int[] nums) {
        long[][] f = new long[2][2];
        for (int x : nums) {
            x %= 2;
            f[x][1] = (f[x][1] + f[x][0]) % MOD;
            f[x][0] = (f[x][0] + f[x ^ 1][0] + f[x ^ 1][1] + 1) % MOD;
        }
        return (int) ((f[0][0] + f[0][1] + f[1][0] + f[1][1]) % MOD);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(countStableSubsequences(nums));
    }
}
