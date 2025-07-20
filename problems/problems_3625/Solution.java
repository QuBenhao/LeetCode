package problems.problems_3625;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countTrapezoids(int[][] points) {
        Map<Double, Map<Double, Integer>> cnt = new HashMap<>();
        Map<Integer, Map<Double, Integer>> cnt2 = new HashMap<>();
        int n = points.length;
        for (int i = 0; i < n - 1; ++i) {
            int x = points[i][0], y = points[i][1];
            for (int j = i + 1; j < n; ++j) {
                int x2 = points[j][0], y2 = points[j][1];
                double k, b;
                if (x2 == x) {
                    k = Double.MAX_VALUE;
                    b = x;
                } else {
                    k = (double) (y2 - y) / (x2 - x);
                    b = (double) (y * (x2 - x) - x * (y2 - y)) / (x2 - x);
                }
                if (k == -0.0) {
                    k = 0.0;
                }
                if (b == -0.0) {
                    b = 0.0;
                }
                cnt.putIfAbsent(k, new HashMap<>());
                cnt.get(k).put(b, cnt.get(k).getOrDefault(b, 0) + 1);
                int mask = (x + x2 + 2000) << 16 | (y + y2 + 2000);
                cnt2.putIfAbsent(mask, new HashMap<>());
                cnt2.get(mask).put(k, cnt2.get(mask).getOrDefault(k, 0) + 1);
            }
        }
        int ans = 0;
        for (Map<Double, Integer> m: cnt.values()) {
            int s = 0;
            for (int v: m.values()) {
                ans += s * v;
                s += v;
            }
        }
        for (Map<Double, Integer> m: cnt2.values()) {
            int s = 0;
            for (int v: m.values()) {
                ans -= s * v;
                s += v;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] points = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(countTrapezoids(points));
    }
}
