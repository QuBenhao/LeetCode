package problems.problems_1304;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] sumZero(int n) {
        int[] ans = new int[n];
        for (int i = 0; i * 2 + 1 < n; ++i) {
            ans[i * 2] = -i - 1;
            ans[i * 2 + 1] = i + 1;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(sumZero(n));
    }
}
