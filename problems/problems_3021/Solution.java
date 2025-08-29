package problems.problems_3021;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long flowerGame(int n, int m) {
        return 1L * (n / 2) * ((m + 1) / 2) + 1L * ((n + 1) / 2) * (m / 2);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int m = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(flowerGame(n, m));
    }
}
