package problems.problems_3405;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int MOD = 1000000007;

    private int fastPow(long base, int exp) {
        long result = 1;
        while (exp > 0) {
            if ((exp & 1) == 1) {
                result = (result * base) % MOD;
            }
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return (int) result;
    }

    private int comb(int n, int k) {
        if (k > n) return 0;
        if (k == 0 || k == n) return 1;

        long numerator = 1;
        long denominator = 1;
        for (int i = 0; i < k; i++) {
            numerator = (numerator * (n - i)) % MOD;
            denominator = (denominator * (i + 1)) % MOD;
        }

        return (int) ((numerator * fastPow(denominator, MOD - 2)) % MOD);
    }

    public int countGoodArrays(int n, int m, int k) {
        long res = m;
        res = (res * fastPow(m-1, n-k-1)) % MOD;
        res = (res * comb(n-1, k)) % MOD;
        return (int) res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int m = Integer.parseInt(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(countGoodArrays(n, m, k));
    }
}
