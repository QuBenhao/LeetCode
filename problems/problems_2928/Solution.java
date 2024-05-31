package problems.problems_2928;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int distributeCandies(int n, int limit) {

    }

    @Override
    public Object solve(String[] values) {
        int n = Integer.parseInt(values[0]);
		int limit = Integer.parseInt(values[1]);
        return JSON.toJSON(distributeCandies(n, limit));
    }
}
