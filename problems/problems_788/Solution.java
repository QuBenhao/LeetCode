package problems.problems_788;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int[] ans = new int[10001];
    static {
        for (int i = 1; i <= 10000; ++i) {
            boolean notRotatable = false;
            boolean diffRotatable = false;
            for (int j = i; j > 0; j /= 10) {
                int c = j % 10;
                if (c == 3 || c == 4 || c == 7) {
                    notRotatable = true;
                    break;
                }
                if (c == 2 || c == 5 || c == 6 || c == 9) {
                    diffRotatable = true;
                }
            }
            ans[i] = ans[i - 1] + (!notRotatable && diffRotatable ? 1 : 0);
        }
    }

    public int rotatedDigits(int n) {
        return ans[n];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(rotatedDigits(n));
    }
}
