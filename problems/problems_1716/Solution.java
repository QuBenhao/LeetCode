package problems.problems_1716;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int totalMoney(int n) {
        int d = n / 7, r = n % 7;
        return 28 * d + (d - 1) * d * 7 / 2 + r * (d + 1 + d + r) / 2;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(totalMoney(n));
    }
}
