package problems.problems_3650;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minCost(int n, int[][] edges) {
        Map<Integer, Integer>[] graph = new HashMap[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new HashMap<>();
        }
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], cost = edge[2];
            graph[u].put(v, Math.min(graph[u].getOrDefault(v, Integer.MAX_VALUE), cost));
            graph[v].put(u, Math.min(graph[v].getOrDefault(u, Integer.MAX_VALUE), cost * 2));
        }
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[0] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, 0}); // {cost, node}
        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int cost = current[0], node = current[1];
            if (node == n - 1) return cost; // If we reached the last node
            if (cost > dist[node]) continue; // Skip if we already found a better path
            for (Map.Entry<Integer, Integer> entry : graph[node].entrySet()) {
                int neighbor = entry.getKey();
                int edgeCost = entry.getValue();
                if (cost + edgeCost < dist[neighbor]) {
                    dist[neighbor] = cost + edgeCost;
                    pq.offer(new int[]{dist[neighbor], neighbor});
                }
            }
        }
        return -1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(minCost(n, edges));
    }
}
