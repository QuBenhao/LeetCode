package problems.problems_3621;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int[] DEPTHS;
    static {
        long maxN = (long) 1e15;
        int bitLength = Long.SIZE - Long.numberOfLeadingZeros(maxN);
        DEPTHS = new int[bitLength + 1];
        for (int i = 2; i <= bitLength; ++i) {
            int j = i;
            while (j > 1) {
                ++DEPTHS[i];
                j = Integer.bitCount(j);
            }
        }
    }

    private long dfs(int pos, boolean isLimit, int counts, int length, long n, long[][][] cache) {
        if (counts < 0 || length - pos < counts) {
            return 0;
        }
        if (pos == length) {
            return 1;
        }
        int intLimit = isLimit ? 1 : 0;
        if (cache[pos][intLimit][counts] != -1) {
            return cache[pos][intLimit][counts];
        }
        long ans = 0;
        int maxDigit = isLimit ? (int) ((n >> (length - pos - 1)) & 1) : 1;
        for (int d = 0; d <= maxDigit; ++d) {
            ans += dfs(pos + 1, isLimit && (d == maxDigit), counts - d, length, n, cache);
        }
        cache[pos][intLimit][counts] = ans;
        return ans;
    }

    public long popcountDepth(long n, int k) {
        if (k == 0) {
            return 1;
        }
        int length = Long.SIZE - Long.numberOfLeadingZeros(n);
        long[][][] cache = new long[length + 1][2][length + 1];
        for (int i = 0; i <= length; ++i) {
            for (int j = 0; j < 2; ++j) {
                Arrays.fill(cache[i][j], -1);
            }
        }
        long ans = 0;
        for (int i = 2; i <= length; ++i) {
            if (DEPTHS[i] + 1 == k) {
                ans += dfs(0, true, i, length, n, cache);
            }
        }
        if (k == 1) {
            ans += dfs(0, true, 1, length, n, cache) - 1;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        long n = Long.parseLong(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(popcountDepth(n, k));
    }
}
