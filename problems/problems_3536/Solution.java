package problems.problems_3536;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxProduct(int n) {
        int mx = 0, sub = 0;
        while (n > 0) {
            int cur = n % 10;
            n /= 10;
            if (cur > mx) {
                sub = mx;
                mx = cur;
            } else if (cur > sub) {
                sub = cur;
            }
        }
        return mx * sub;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(maxProduct(n));
    }
}
