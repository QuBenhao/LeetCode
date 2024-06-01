package problems.problems_2928;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int combinationTwo(int n) {
        return n > 1 ? n * (n - 1) / 2 : 0;
    }

    public int distributeCandies(int n, int limit) {
        return combinationTwo(n + 2) - 3 * combinationTwo(n + 1 - limit) + 3 * combinationTwo(n - limit * 2) - combinationTwo(n - 1 - limit * 3);
    }

    @Override
    public Object solve(String[] values) {
        int n = Integer.parseInt(values[0]);
		int limit = Integer.parseInt(values[1]);
        return JSON.toJSON(distributeCandies(n, limit));
    }
}
