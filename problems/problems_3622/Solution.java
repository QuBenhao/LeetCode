package problems.problems_3622;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean checkDivisibility(int n) {
        int s = 0, m = 1;
        for (int num = n; num > 0; num /= 10) {
            s += num % 10;
            m *= num % 10;
        }
        return n % (s + m) == 0;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(checkDivisibility(n));
    }
}
