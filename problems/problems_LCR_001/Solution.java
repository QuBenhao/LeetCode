package problems.problems_LCR_001;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int divide(int a, int b) {
        if (a == Integer.MIN_VALUE && b == -1) {
            return Integer.MAX_VALUE;
        }
        long dividend = Math.abs((long) a), divisor = Math.abs((long) b), ans = 0;
        for (int i = 31; i >= 0; i--) {
            if ((dividend >> i) >= divisor) {
                ans |= 1L << i;
                dividend -= divisor << i;
            }
        }
        return (a > 0) == (b > 0) ? (int) ans : (int) -ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int a = Integer.parseInt(inputJsonValues[0]);
		int b = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(divide(a, b));
    }
}
