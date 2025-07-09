package problems.problems_670;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumSwap(int num) {
        List<Integer> digits = new ArrayList<>();
        int[] idxes = new int[10];
        Arrays.fill(idxes, -1);
        int n = 0;
        for (int x = num; x > 0; x /= 10) {
            int digit = x % 10;
            digits.add(digit);
            if (idxes[digit] < 0) {
                idxes[digit] = n;
            }
            ++n;
        }
        for (int i = n - 1; i > 0; --i) {
            for (int d = 9; d > digits.get(i); --d) {
                if (idxes[d] >= 0 && idxes[d] < i) {
                    Collections.swap(digits, i, idxes[d]);
                    int result = 0;
                    for (int j = n - 1; j >= 0; --j) {
                        result = result * 10 + digits.get(j);
                    }
                    return result;
                }
            }
        }
        return num;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int num = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(maximumSwap(num));
    }
}
