package problems.problems_3372;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private Map<Integer, List<Integer>> buildTree(int[][] edges) {
        Map<Integer, List<Integer>> map = new HashMap<>(edges.length + 1);
        for (int[] edge: edges) {
            int u = edge[0], v = edge[1];
            List<Integer> lu = map.getOrDefault(u, new ArrayList<>());
            List<Integer> lv = map.getOrDefault(v, new ArrayList<>());
            map.put(u, lu);
            map.put(v, lv);
            lu.add(v);
            lv.add(u);
        }
        return map;
    }

    private int dfs(int node, int pa, int k, Map<Integer, List<Integer>> graph) {
        if (k < 0) {
            return 0;
        }
        if (k == 0) {
            return 1;
        }
        k--;
        int res = 1;
        for (int neigh: graph.get(node)) {
            if (neigh == pa) {
                continue;
            }
            res += dfs(neigh, node, k, graph);
        }
        return res;
    }

    public int[] maxTargetNodes(int[][] edges1, int[][] edges2, int k) {
        Map<Integer, List<Integer>> t2 = buildTree(edges2);
        int max2 = 0;
        for (int i = 0; i < edges2.length + 1; i++) {
            max2 = Math.max(max2, dfs(i, -1, k-1, t2));
        }
        int[] ans = new int[edges1.length + 1];
        Map<Integer, List<Integer>> t1 = buildTree(edges1);
        for (int i = 0; i < edges1.length + 1; i++) {
            ans[i] = dfs(i, -1, k, t1) + max2;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] edges1 = jsonArrayToInt2DArray(inputJsonValues[0]);
		int[][] edges2 = jsonArrayToInt2DArray(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maxTargetNodes(edges1, edges2, k));
    }
}
