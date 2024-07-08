package problems.problems_3102;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumDistance(int[][] points) {
        final int INF = Integer.MAX_VALUE;
        int maxX1 = -INF, maxX2 = -INF, maxY1 = -INF, maxY2 = -INF;
        int minX1 = INF, minX2 = INF, minY1 = INF, minY2 = INF;

        for (int[] p : points) {
            int x = p[0] + p[1];
            int y = p[1] - p[0];

            // x 最大次大
            if (x > maxX1) {
                maxX2 = maxX1;
                maxX1 = x;
            } else if (x > maxX2) {
                maxX2 = x;
            }

            // x 最小次小
            if (x < minX1) {
                minX2 = minX1;
                minX1 = x;
            } else if (x < minX2) {
                minX2 = x;
            }

            // y 最大次大
            if (y > maxY1) {
                maxY2 = maxY1;
                maxY1 = y;
            } else if (y > maxY2) {
                maxY2 = y;
            }

            // y 最小次小
            if (y < minY1) {
                minY2 = minY1;
                minY1 = y;
            } else if (y < minY2) {
                minY2 = y;
            }
        }

        int ans = INF;
        for (int[] p : points) {
            int x = p[0] + p[1];
            int y = p[1] - p[0];
            int dx = (x == maxX1 ? maxX2 : maxX1) - (x == minX1 ? minX2 : minX1);
            int dy = (y == maxY1 ? maxY2 : maxY1) - (y == minY1 ? minY2 : minY1);
            ans = Math.min(ans, Math.max(dx, dy));
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] points = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(minimumDistance(points));
    }
}
