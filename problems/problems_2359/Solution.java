package problems.problems_2359;

import java.util.Arrays;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private void dfs(int[] edges, int node, int[] dis) {
        int d = 0;
        for (int cur = node; cur != -1 && dis[cur] == -1; cur = edges[cur]) {
            dis[cur] = d++;
        }
    }

    public int closestMeetingNode(int[] edges, int node1, int node2) {
        int n = edges.length;
        int[] dis1 = new int[n];
        int[] dis2 = new int[n];
        Arrays.fill(dis1, -1);
        Arrays.fill(dis2, -1);
        dfs(edges, node1, dis1);
        dfs(edges, node2, dis2);
        int ans = -1, ansD = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (dis1[i] == -1 || dis2[i] == -1) {
                continue;
            }
            int d = Math.max(dis1[i], dis2[i]);
            if (d < ansD) {
                ans = i;
                ansD = d;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] edges = jsonArrayToIntArray(inputJsonValues[0]);
		int node1 = Integer.parseInt(inputJsonValues[1]);
		int node2 = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(closestMeetingNode(edges, node1, node2));
    }
}
