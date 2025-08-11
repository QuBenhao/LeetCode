package problems.problems_2438;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int MOD = 1_000_000_007;
    private static final int[] POWERS = new int[436];
    static {
        POWERS[0] = 1;
        for (int i = 1; i < 436; i++) {
            POWERS[i] = (POWERS[i - 1] * 2) % MOD;
        }
    }
    public int[] productQueries(int n, int[][] queries) {
        List<Integer> preSum = new ArrayList<>();
        preSum.add(0);
        while (n > 0) {
            int lowbit = n & -n;
            int length = 31 - Integer.numberOfLeadingZeros(lowbit);
            preSum.add(preSum.getLast() + length);
            n ^= lowbit;
        }
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int left = queries[i][0];
            int right = queries[i][1];
            ans[i] = POWERS[preSum.get(right + 1) - preSum.get(left)];
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] queries = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(productQueries(n, queries));
    }
}
