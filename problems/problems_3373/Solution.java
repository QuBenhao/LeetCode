package problems.problems_3373;

import java.util.ArrayList;
import java.util.List;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private List<List<Integer>> buildTree(int[][] edges) {
        List<List<Integer>> g = new ArrayList<>(edges.length+1);
        for (int i = 0; i < edges.length+1; i++) {
            g.add(new ArrayList<>());
        }
        for (int[] edge: edges) {
            int u = edge[0], v = edge[1];
            g.get(u).add(v);
            g.get(v).add(u);
        }
        return g;
    }

    private int dfs(List<List<Integer>> graph, int node, int pa, int d) {
        int ans = d == 0 ? 1 : 0;
        d ^= 1;
        for (int neigh: graph.get(node)) {
            if (neigh != pa) {
                ans += dfs(graph, neigh, node, d);
            }
        }
        return ans;
    }

    private void dfs2(List<List<Integer>> graph, int node, int pa, int[] ans, int m, int max2) {
        int cur = m - ans[node] + max2 * 2;
        for (int neigh: graph.get(node)) {
            if (neigh != pa) {
                ans[neigh] = cur;
                dfs2(graph, neigh, node, ans, m, max2);
            }
        }
    }

    public int[] maxTargetNodes(int[][] edges1, int[][] edges2) {
        var graph1 = buildTree(edges1);
        var graph2 = buildTree(edges2);

        int m = graph1.size(), n = graph2.size();
        int d0 = dfs(graph2, 0, -1, 0);
        int max2 = Math.max(d0, n-d0);
        int[] ans = new int[m];
        ans[0] = dfs(graph1, 0, -1, 0) + max2;
        dfs2(graph1, 0, -1, ans, m, max2);
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] edges1 = jsonArrayToInt2DArray(inputJsonValues[0]);
		int[][] edges2 = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(maxTargetNodes(edges1, edges2));
    }
}
