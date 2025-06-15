package problems.problems_3585;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {

    class TreeAncestor {
        public final int[][] pa;
        private final int[] depth;
        public final long[] distance;
        private final int m;

        private void dfs(int node, int parent, Map<Integer, Integer>[] graph) {
            pa[node][0] = parent;
            if (graph[node] == null) {
                return;
            }
            // graph foreach
            for (Map.Entry<Integer, Integer> entry : graph[node].entrySet()) {
                int c = entry.getKey(), w = entry.getValue();
                if (c == parent) continue;
                depth[c] = depth[node] + 1;
                distance[c] = distance[node] + w;
                dfs(c, node, graph);
            }
        }
        public TreeAncestor(int[][] edges) {
            int n = edges.length + 1;
            m = 32 - Integer.numberOfLeadingZeros(n);

            pa = new int[n][m];
            depth = new int[n];
            Arrays.fill(depth, 0);
            distance = new long[n];
            Arrays.fill(distance, 0);

            Map<Integer, Integer>[] graph = new Map[n];
            for (int[] edge : edges) {
                int u = edge[0], v = edge[1], w = edge[2];
                graph[u] = graph[u] == null ? new HashMap<>() : graph[u];
                graph[u].put(v, w);
                graph[v] = graph[v] == null ? new HashMap<>() : graph[v];
                graph[v].put(u, w);
            }

            dfs(0, -1, graph);

            for (int j = 1; j < m; j++) {
                for (int i = 0; i < n; i++) {
                    if (pa[i][j - 1] != -1) {
                        pa[i][j] = pa[pa[i][j - 1]][j - 1];
                    } else {
                        pa[i][j] = -1;
                    }
                }
            }
        }

        public int getKthAncestor(int node, int k) {
            for (; node != -1 && k > 0; k &= k - 1) {
                node = pa[node][Integer.numberOfTrailingZeros(k&-k)];
            }
            return node;
        }

        public int getLCA(int u, int v) {
            if (depth[u] > depth[v]) {
                int tmp = u;
                u = v;
                v = tmp;
            }
            v = getKthAncestor(v, depth[v] - depth[u]);
            if (v == u) {
                return u;
            }
            for (int j = m - 1; j >= 0; j--) {
                if (pa[u][j] != pa[v][j]) {
                    u = pa[u][j];
                    v = pa[v][j];
                }
            }
            return pa[u][0];
        }

        public int findDistance(int u, long d) {
            d = distance[u] - d;
            for (int j = m-1; j >= 0; --j) {
                int p = pa[u][j];
                if (p != -1 && distance[p] >= d) {
                    u = p;
                }
            }
            return u;
        }
    }

    public int[] findMedian(int n, int[][] edges, int[][] queries) {
        TreeAncestor ta = new TreeAncestor(edges);
        int[] result = new int[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0], v = queries[i][1];
            if (u == v) {
                result[i] = u;
                continue;
            }
            int lca = ta.getLCA(u, v);
            long totalDis = ta.distance[u] + ta.distance[v] - 2 * ta.distance[lca];
            long halfDis = (totalDis + 1) / 2;
            if (ta.distance[u] - ta.distance[lca] >= halfDis) {
                int x = ta.findDistance(u, halfDis-1);
                result[i] = ta.pa[x][0];
            } else {
                result[i] = ta.findDistance(v, totalDis - halfDis);
            }
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		int[][] queries = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(findMedian(n, edges, queries));
    }
}
