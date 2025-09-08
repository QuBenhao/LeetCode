package problems.problems_1317;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] getNoZeroIntegers(int n) {
        int a = 0;
        int base = 1;
        int x = n;
        while (x > 1) {
            int d = x % 10;
            x /= 10;
            if (d <= 1) {
                x -= 1;
                d += 10;
            }
            a += d / 2 * base;
            base *= 10;
        }
        return new int[]{a, n - a};
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(getNoZeroIntegers(n));
    }
}
