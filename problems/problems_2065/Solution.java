package problems.problems_2065;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximalPathQuality(int[] values, int[][] edges, int maxTime) {
        int n = values.length;
        List<int[]>[] g = new ArrayList[n];
        Arrays.setAll(g, i -> new ArrayList<>());
        for (int[] e : edges) {
            int x = e[0];
            int y = e[1];
            int t = e[2];
            g[x].add(new int[]{y, t});
            g[y].add(new int[]{x, t});
        }

        // Dijkstra's algorithm
        int[] dis = new int[n];
        Arrays.fill(dis, Integer.MAX_VALUE);
        dis[0] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        pq.add(new int[]{0, 0});
        while (!pq.isEmpty()) {
            int[] p = pq.poll();
            int dx = p[0];
            int x = p[1];
            if (dx > dis[x]) { // x was already popped from the heap
                continue;
            }
            for (int[] e : g[x]) {
                int y = e[0];
                int newDis = dx + e[1];
                if (newDis < dis[y]) {
                    dis[y] = newDis; // Update the shortest distances to x's neighbors
                    pq.offer(new int[]{newDis, y});
                }
            }
        }

        boolean[] vis = new boolean[n];
        vis[0] = true;
        return dfs(0, 0, values[0], vis, g, values, maxTime, dis);
    }

    private int dfs(int x, int sumTime, int sumValue, boolean[] vis, List<int[]>[] g, int[] values, int maxTime, int[] dis) {
        int res = x == 0 ? sumValue : 0;
        for (int[] e : g[x]) {
            int y = e[0];
            int t = e[1];
            // Compared with method 1, this also includes dis[y]
            if (sumTime + t + dis[y] > maxTime) {
                continue;
            }
            if (vis[y]) {
                res = Math.max(res, dfs(y, sumTime + t, sumValue, vis, g, values, maxTime, dis));
            } else {
                vis[y] = true;
                // Count each node's value at most once in the total
                res = Math.max(res, dfs(y, sumTime + t, sumValue + values[y], vis, g, values, maxTime, dis));
                vis[y] = false; // Restore the previous state
            }
        }
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] values = jsonArrayToIntArray(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		int maxTime = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maximalPathQuality(values, edges, maxTime));
    }
}
