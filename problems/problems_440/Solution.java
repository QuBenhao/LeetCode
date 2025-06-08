package problems.problems_440;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int dfs(long n, long l, long r) {
        if (l > n) {
            return 0;
        }
        return Math.toIntExact(Math.min(n, r) - l + 1 + dfs(n, l * 10, r * 10 + 9));
    }
    public int findKthNumber(int n, int k) {
        int cur = 1;
        while (k > 1) {
            int count = dfs(n, cur, cur);
            if (count < k) {
                k -= count;
                cur++;
            } else {
                k--;
                cur *= 10;
            }
        }
        return cur;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(findKthNumber(n, k));
    }
}
