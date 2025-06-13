package problems.problems_3532;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;

public class Solution extends BaseSolution {
    class UnionFind {
        private int[] parent;
        private int[] size;
        private int count;

        public UnionFind(int n) {
            parent = new int[n];
            size = new int[n];
            count = n;
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        public int find(int x) {
            if (parent[x] != x) {
                parent[x] = find(parent[x]); // Path compression
            }
            return parent[x];
        }

        public boolean union(int x, int y) {
            int px = find(x);
            int py = find(y);
            if (px == py) {
                return false; // Already in the same set
            }
            if (size[px] < size[py]) {
                parent[px] = py;
                size[py] += size[px];
            } else {
                parent[py] = px;
                size[px] += size[py];
            }
            count--;
            return true; // Union successful
        }

        public int getCount() {
            return count;
        }
    }

    public boolean[] pathExistenceQueries(int n, int[] nums, int maxDiff, int[][] queries) {
        UnionFind uf = new UnionFind(n);
        for (int i = 0; i < n - 1; i++) {
            if (nums[i+1] - nums[i] <= maxDiff) {
                uf.union(i, i + 1);
            }
        }
        boolean[] results = new boolean[queries.length];
        for (int i = 0; i < queries.length; i++) {
            int u = queries[i][0];
            int v = queries[i][1];
            results[i] = uf.find(u) == uf.find(v);
        }
        return results;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[] nums = jsonArrayToIntArray(inputJsonValues[1]);
		int maxDiff = Integer.parseInt(inputJsonValues[2]);
		int[][] queries = jsonArrayToInt2DArray(inputJsonValues[3]);
        return JSON.toJSON(pathExistenceQueries(n, nums, maxDiff, queries));
    }
}
