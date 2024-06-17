package problems.problems_50;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double myPow(double x, int n) {
        if (x == 0.0) {
            return 0.0;
        }
        double ans = 1.0;
        if (n < 0) {
            x = 1.0 / x;
            if (n == Integer.MIN_VALUE) {
                ans = x;
                n = Integer.MAX_VALUE;
            } else {
                n = -n;
            }
        }
        while (n > 0) {
            if ((n & 1) == 1) {
                ans *= x;
            }
            x *= x;
            n >>= 1;
        }
        return ans;
    }


    @Override
    public Object solve(String[] values) {
        double x = Double.parseDouble(values[0]);
        int n = Integer.parseInt(values[1]);
        return JSON.toJSON(myPow(x, n));
    }
}
