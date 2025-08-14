package problems.problems_342;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isPowerOfFour(int n) {
        if (n <= 0 || (n & (n - 1)) != 0) {
            return false;
        }
        return (n - 1) % 3 == 0;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(isPowerOfFour(n));
    }
}
