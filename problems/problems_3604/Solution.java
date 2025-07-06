package problems.problems_3604;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minTime(int n, int[][] edges) {
        List<List<int[]>> graph = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], st = edge[2], et = edge[3];
            graph.get(u).add(new int[]{v, st, et});
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0])); // Min-heap based on time
        pq.offer(new int[]{0, 0}); // {time, node}
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[0] = 0;
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int time = curr[0], node = curr[1];
            if (node == n - 1) return time; // If we reached the last node, return the time
            if (time > dist[node]) continue; // Skip if we have already found a better time
            for (int[] neighbor : graph.get(node)) {
                int nextNode = neighbor[0], startTime = neighbor[1], endTime = neighbor[2];
                if (time <= endTime) {
                    int nextTime = Math.max(time, startTime) + 1; // Move to the next time step
                    if (nextTime < dist[nextNode]) {
                        dist[nextNode] = nextTime;
                        pq.offer(new int[]{nextTime, nextNode});
                    }
                }
            }
        }
        return -1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(minTime(n, edges));
    }
}
