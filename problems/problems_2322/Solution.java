package problems.problems_2322;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int time;

    private int dfs(int node, int parent, List<Integer>[] graph, int[] nums, int[] xorSum, int[] timeIn, int[] timeOut) {
        timeIn[node] = time++;
        xorSum[node] = nums[node];
        for (int neighbor : graph[node]) {
            if (neighbor != parent) {
                xorSum[node] ^= dfs(neighbor, node, graph, nums, xorSum, timeIn, timeOut);
            }
        }
        timeOut[node] = time++;
        return xorSum[node];
    }

    public int minimumScore(int[] nums, int[][] edges) {
        int n = nums.length;
        List<Integer>[] graph = new List[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }
        for (int[] edge : edges) {
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }
        int[] xorSum = new int[n];
        int[] timeIn = new int[n];
        int[] timeOut = new int[n];
        time = 0;
        dfs(0, -1, graph, nums, xorSum, timeIn, timeOut);
        int ans = Integer.MAX_VALUE;
        for (int x = 1; x < n - 1; ++x) {
            for (int y = x + 1; y < n; ++y) {
                int a, b, c;
                if (timeIn[x] < timeIn[y] && timeOut[x] > timeOut[y]) {
                    a = xorSum[y];
                    b = xorSum[x] ^ a;
                    c = xorSum[0] ^ xorSum[x];
                } else if (timeIn[y] < timeIn[x] && timeOut[y] > timeOut[x]) {
                    a = xorSum[x];
                    b = xorSum[y] ^ a;
                    c = xorSum[0] ^ xorSum[y];
                } else {
                    a = xorSum[x];
                    b = xorSum[y];
                    c = xorSum[0] ^ a ^ b;
                }
                ans = Math.min(ans, Math.max(a, Math.max(b, c)) - Math.min(a, Math.min(b, c)));
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(minimumScore(nums, edges));
    }
}
