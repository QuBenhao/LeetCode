package premiums.premiums_1056;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean confusingNumber(int n) {
        Map<Integer, Integer> trans = new HashMap<>(5);
        trans.put(0, 0);
        trans.put(1, 1);
        trans.put(6, 9);
        trans.put(8, 8);
        trans.put(9, 6);
        int revert = 0;
        for (int num = n; num > 0; num /= 10) {
            int cur = num % 10;
            if (!trans.containsKey(cur)) {
                return false;
            }
            revert = 10 * revert + trans.get(cur);
        }
        return revert != n;
    }

    @Override
    public Object solve(String[] values) {
        int n = Integer.parseInt(values[0]);
        return JSON.toJSON(confusingNumber(n));
    }
}
