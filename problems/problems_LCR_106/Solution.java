package problems.problems_LCR_106;

import java.util.Arrays;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isBipartite(int[][] graph) {
        int n = graph.length;
        int[] color = new int[n];
        Arrays.fill(color, -1);
        for (int i = 0; i < n; i++) {
            if (color[i] != -1) {
                continue;
            }
            if (!dfs(graph, color, i, 0)) {
                return false;
            }
        }
        return true;
    }

    private boolean dfs(int[][] graph, int[] color, int node, int c) {
        if (color[node] != -1) {
            return color[node] == c;
        }
        color[node] = c;
        int nxt = 1 ^ c;
        for (int other: graph[node]) {
            if (!dfs(graph, color, other, nxt)) {
                return false;
            }
        }
        return true;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] graph = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(isBipartite(graph));
    }
}
