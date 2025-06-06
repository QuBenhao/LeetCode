package problems.problems_2929;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private long combination2(int n) {
        return n > 1 ? (long) n * (n - 1) / 2 : 0;
    }

    public long distributeCandies(int n, int limit) {
        return combination2(n+2) - 3 * combination2(n - limit + 1) 
               + 3 * combination2(n - 2 * limit) - combination2(n - 3 * limit - 1);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int limit = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(distributeCandies(n, limit));
    }
}
