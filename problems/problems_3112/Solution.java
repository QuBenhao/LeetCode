package problems.problems_3112;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] minimumTime(int n, int[][] edges, int[] disappear) {
        List<int[]>[] graph = new ArrayList[n];
        Arrays.setAll(graph, i -> new ArrayList<>());
        for (int[] edge : edges) {
            graph[edge[0]].add(new int[]{edge[1], edge[2]});
            graph[edge[1]].add(new int[]{edge[0], edge[2]});
        }
        int[] ans = new int[n];
        Arrays.fill(ans, -1);
        ans[0] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, 0});
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int u = cur[1];
            if (ans[u] < cur[0]) {
                continue;
            }
            for (int[] next : graph[u]) {
                int v = next[0];
                int w = next[1];
                int nd = cur[0] + w;
                if (nd < disappear[v] && (ans[v] == -1 || ans[v] > nd)) {
                    ans[v] = nd;
                    pq.offer(new int[]{nd, v});
                }
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		int[] disappear = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(minimumTime(n, edges, disappear));
    }
}
