package problems.problems_667;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] constructArray(int n, int k) {
        int[] result = new int[n];
        for (int i = 0; i <= k; ++i) {
            if (i % 2 == 0) {
                result[i] = i / 2 + 1;
            } else {
                result[i] = k - i / 2 + 1;
            }
        }
        for (int i = k + 2; i <= n; ++i) {
            result[i-1] = i;
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(constructArray(n, k));
    }
}
