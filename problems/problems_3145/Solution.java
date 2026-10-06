package problems.problems_3145;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] findProductsOfElements(long[][] queries) {
        int[] ans = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            long[] q = queries[i];
            long er = sumE(q[1] + 1);
            long el = sumE(q[0]);
            ans[i] = pow(2, er - el, q[2]);
        }
        return ans;
    }

    private long sumE(long k) {
        long res = 0;
        long n = 0;
        long cnt1 = 0; // Number of ones already placed
        long sumI = 0; // Sum of exponents for the ones already placed
        for (long i = 63 - Long.numberOfLeadingZeros(k + 1); i > 0; i--) {
            long c = (cnt1 << i) + (i << (i - 1)); // Number of additional exponents
            if (c <= k) {
                k -= c;
                res += (sumI << i) + ((i * (i - 1) / 2) << (i - 1));
                sumI += i;
                cnt1++;
                n |= 1L << i; // Place a 1
            }
        }
        // Handle the lowest bit separately
        if (cnt1 <= k) {
            k -= cnt1;
            res += sumI;
            n |= 1; // Set the lowest bit to 1
        }
        // Supply the remaining k exponents from the k lowest set bits of n
        while (k-- > 0) {
            res += Long.numberOfTrailingZeros(n);
            n &= n - 1; // Clear the lowest set bit (set it to 0)
        }
        return res;
    }

    private int pow(long x, long n, long mod) {
        long res = 1 % mod;
        for (; n > 0; n /= 2) {
            if (n % 2 == 1) {
                res = res * x % mod;
            }
            x = x * x % mod;
        }
        return (int) res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        long[][] queries = jsonArrayToLong2DArray(inputJsonValues[0]);
        return JSON.toJSON(findProductsOfElements(queries));
    }
}
