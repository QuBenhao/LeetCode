package problems.problems_3620;

import com.alibaba.fastjson.JSON;
import java.util.*;

import javafx.util.Pair;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private boolean canReach(List<Pair<Integer, Integer>>[] graph, int n, int mid, long k) {
        long[] distance = new long[n];
        Arrays.fill(distance, Long.MAX_VALUE);
        distance[0] = 0;
        PriorityQueue<Pair<Long, Integer>> pq = new PriorityQueue<>(Comparator.comparingLong(Pair::getKey));
        pq.offer(new Pair<>(0L, 0)); // (distance, node)
        while (!pq.isEmpty()) {
            Pair<Long, Integer> current = pq.poll();
            long dist = current.getKey();
            int node = current.getValue();
            if (node == n - 1) {
                return true;
            }
            if (dist > distance[node]) continue; // Skip if we already found a better path

            for (Pair<Integer, Integer> neighbor : graph[node]) {
                int nextNode = neighbor.getKey();
                int cost = neighbor.getValue();
                if (cost < mid) continue; // Skip edges with cost less than mid

                long newDist = dist + cost;
                if (newDist <= k && newDist < distance[nextNode]) {
                    distance[nextNode] = newDist;
                    pq.offer(new Pair<>(newDist, nextNode));
                }
            }
        }
        return false;
    }

    public int findMaxPathScore(int[][] edges, boolean[] online, long k) {
        int n = online.length;
        List<Pair<Integer, Integer>>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        int right = 0;
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], c = edge[2];
            if (online[u] && online[v]) {
                graph[u].add(new Pair<>(v, c));
                right = Math.max(right, c);
            }
        }
        for (int left = -1; left < right; ) {
            int mid = (left + right + 1) / 2;
            if (canReach(graph, n, mid, k)) {
                left = mid; // mid is feasible
            } else {
                right = mid - 1; // mid is not feasible
            }
        }
        return right;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] edges = jsonArrayToInt2DArray(inputJsonValues[0]);
		boolean[] online = jsonArrayToBooleanArray(inputJsonValues[1]);
		long k = Long.parseLong(inputJsonValues[2]);
        return JSON.toJSON(findMaxPathScore(edges, online, k));
    }
}
