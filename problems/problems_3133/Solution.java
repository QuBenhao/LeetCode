package problems.problems_3133;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minEnd(int n, int x) {
        long ans = x;
        n--;
        for (int i = 0, j = 0; n >> j > 0; i++) {
            if ((ans >> i & 1) == 0) {
                ans |= (1L & (n >> j)) << i;
                j++;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int x = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minEnd(n, x));
    }
}
