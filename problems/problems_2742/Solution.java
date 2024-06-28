package problems.problems_2742;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int paintWalls(int[] cost, int[] time) {
        int n = cost.length;
        int[] f = new int[n + 1];
        Arrays.fill(f, Integer.MAX_VALUE / 2);
        f[0] = 0;
        for (int i = 0; i < n; i++) {
            int t = time[i] + 1;
            for (int j = n; j > 0; j--) {
                f[j] = Math.min(f[j], f[Math.max(j - t, 0)] + cost[i]);
            }
        }
        return f[n];
    }

    @Override
    public Object solve(String[] values) {
        int[] cost = jsonArrayToIntArray(values[0]);
		int[] time = jsonArrayToIntArray(values[1]);
        return JSON.toJSON(paintWalls(cost, time));
    }
}
