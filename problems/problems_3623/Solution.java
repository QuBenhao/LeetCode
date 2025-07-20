package problems.problems_3623;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int MOD = 1_000_000_007;
    public int countTrapezoids(int[][] points) {
        Map<Integer, Integer> counts = new HashMap<>();
        for (int[] point: points) {
            counts.put(point[1], counts.getOrDefault(point[1], 0) + 1);
        }
        int ans = 0;
        int s = 0;
        for (int v: counts.values()) {
            int total = Math.toIntExact((long) v * (v - 1) / 2 % MOD);
            ans = (Math.toIntExact((long)total * s % MOD) + ans) % MOD;
            s = (s + total) % MOD;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] points = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(countTrapezoids(points));
    }
}
