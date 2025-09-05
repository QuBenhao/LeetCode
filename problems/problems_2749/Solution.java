package problems.problems_2749;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int makeTheIntegerZero(int num1, int num2) {
        long x = num1;
        for (int k = 1;; ++k) {
            x -= num2;
            if (k > x) {
                break;
            }
            if (Long.bitCount(x) <= k) {
                return k;
            }
        }
        return -1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int num1 = Integer.parseInt(inputJsonValues[0]);
		int num2 = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(makeTheIntegerZero(num1, num2));
    }
}
