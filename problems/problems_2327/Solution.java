package problems.problems_2327;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int MOD = (int)1e9 + 7;
    public int peopleAwareOfSecret(int n, int delay, int forget) {
        int[] preSum = new int[n + 1];
        preSum[1] = 1;
        for (int i = 2; i <= n; ++i) {
            int inc = (preSum[Math.max(i - delay, 0)] - preSum[Math.max(i - forget, 0)]) % MOD;
            preSum[i] = (preSum[i - 1] + inc) % MOD;
        }
        return ((preSum[n] - preSum[Math.max(n - forget, 0)]) % MOD + MOD) % MOD;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int delay = Integer.parseInt(inputJsonValues[1]);
		int forget = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(peopleAwareOfSecret(n, delay, forget));
    }
}
