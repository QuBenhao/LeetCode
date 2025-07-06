package problems.problems_3608;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minTime(int n, int[][] edges, int k) {
        Arrays.sort(edges, (a, b) -> Integer.compare(b[2], a[2]));
        UnionFind uf = new UnionFind(n);
        for (int[] edge: edges) {
            uf.union(edge[0], edge[1]);
            if (uf.getCount() < k) {
                return edge[2];
            }
        }
        return 0;
    }

    class UnionFind {
        private final int[] parent;
        private final int[] size;
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

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(minTime(n, edges, k));
    }
}
