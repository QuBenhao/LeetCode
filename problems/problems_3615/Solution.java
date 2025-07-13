package problems.problems_3615;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int dfs(int x, int y, int explored, List<Integer>[] graph, String label, int[][][] dp) {
        if (dp[x][y][explored] != -1) {
            return dp[x][y][explored];
        }
        int ans = 0;
        for (int nx: graph[x]) {
            if (((explored >> nx) & 1) != 0) continue;
            for (int ny: graph[y]) {
                if (nx == ny || ((explored >> ny) & 1) != 0 || label.charAt(nx) != label.charAt(ny)) continue;
                if (nx > ny) {
                    ans = Math.max(ans, dfs(ny, nx, explored | (1 << nx) | (1 << ny), graph, label, dp) + 2);
                } else {
                    ans = Math.max(ans, dfs(nx, ny, explored | (1 << nx) | (1 << ny), graph, label, dp) + 2);
                }
            }
        }
        dp[x][y][explored] = ans;
        return ans;
    }

    public int maxLen(int n, int[][] edges, String label) {
        List<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; ++i) {
            graph[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }
        int maxN = 1 << n;
        int[][][] dp = new int[n][n][maxN];
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                Arrays.fill(dp[i][j], -1);
            }
        }
        int ans = 1;
        for (int i = 0; i < n; ++i) {
            ans = Math.max(ans, dfs(i, i, 1 << i, graph, label, dp) + 1);
            for (int j: graph[i]) {
                if (i > j || label.charAt(i) != label.charAt(j)) continue;
                ans = Math.max(ans, dfs(i, j, (1 << i) | (1 << j), graph, label, dp) + 2);
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		String label = jsonStringToString(inputJsonValues[2]);
        return JSON.toJSON(maxLen(n, edges, label));
    }
}
