package problems.problems_3007;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long findMaximumNumber(long k, int x) {
        long num = 0L, preOne = 0L;
        for (long i = 63 - Long.numberOfLeadingZeros((k + 1) << x); i >= 0; i--) {
            long cur = (preOne << i) + (i / x << i >> 1);
            if (cur <= k) {
                k -= cur;
                num |= 1L << i;
                preOne += (i + 1) % x == 0 ? 1 : 0;
            }
        }
        return num - 1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        long k = Long.parseLong(inputJsonValues[0]);
		int x = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(findMaximumNumber(k, x));
    }
}
