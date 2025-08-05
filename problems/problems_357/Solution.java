package problems.problems_357;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countNumbersWithUniqueDigits(int n) {
        if (n == 0) return 1;
        int ans = 10;
        for (int i = 2, last = 9; i <= n; ++i) {
            int cur = last * (11 - i);
            ans += cur;
            last = cur;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(countNumbersWithUniqueDigits(n));
    }
}
