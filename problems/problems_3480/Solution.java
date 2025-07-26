package problems.problems_3480;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maxSubarrays(int n, int[][] conflictingPairs) {
        int[] g0 = new int[n + 1], g1 = new int[n + 1];
        Arrays.fill(g0, n + 1);
        Arrays.fill(g1, n + 1);
        for (int[] pair : conflictingPairs) {
            int a = pair[0], b = pair[1];
            if (a > b) {
                int temp = a;
                a = b;
                b = temp;
            }
            if (b < g0[a]) {
                g1[a] = g0[a];
                g0[a] = b;
            } else if (b < g1[a]) {
                g1[a] = b;
            }
        }
        long ans = 0, maxExtra = 0, extra = 0;
        int b0 = n + 1, b1 = n + 1;
        for (int i = n; i > 0; --i) {
            int preB = b0;
            int b = g0[i], c = g1[i];
            if (b < b0) {
                b1 = Math.min(b0, c);
                b0 = b;
            } else if (b < b1) {
                b1 = b;
            } else if (c < b1) {
                b1 = c;
            }
            ans += b0 - i;
            if (b0 != preB) {
                extra = 0;
            }
            extra += b1 - b0;
            if (extra > maxExtra) {
                maxExtra = extra;
            }
        }
        return ans + maxExtra;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] conflictingPairs = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(maxSubarrays(n, conflictingPairs));
    }
}
