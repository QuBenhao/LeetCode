package problems.problems_2959;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfSets(int n, int maxDistance, int[][] roads) {
        int[][] g = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(g[i], Integer.MAX_VALUE / 2); // 防止加法溢出
            g[i][i] = 0;
        }
        for (int[] e : roads) {
            int x = e[0], y = e[1], wt = e[2];
            g[x][y] = Math.min(g[x][y], wt);
            g[y][x] = Math.min(g[y][x], wt);
        }

        int ans = 0;
        int[][] f = new int[n][n];
        next:
        for (int s = 0; s < (1 << n); s++) {
            for (int i = 0; i < n; i++) {
                if ((s >> i & 1) == 1) {
                    System.arraycopy(g[i], 0, f[i], 0, n);
                }
            }

            // Floyd
            for (int k = 0; k < n; k++) {
                if ((s >> k & 1) == 0) continue;
                for (int i = 0; i < n; i++) {
                    if ((s >> i & 1) == 0) continue;
                    for (int j = 0; j < n; j++) {
                        f[i][j] = Math.min(f[i][j], f[i][k] + f[k][j]);
                    }
                }
            }

            for (int i = 0; i < n; i++) {
                if ((s >> i & 1) == 0) continue;
                for (int j = 0; j < n; j++) {
                    if ((s >> j & 1) == 1 && f[i][j] > maxDistance) {
                        continue next;
                    }
                }
            }
            ans++;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int maxDistance = Integer.parseInt(inputJsonValues[1]);
		int[][] roads = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(numberOfSets(n, maxDistance, roads));
    }
}
