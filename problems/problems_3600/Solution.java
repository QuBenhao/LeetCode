package problems.problems_3600;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {

    class UnionFind {
        private final int[] parent;
        private final int[] size;
        public int count;

        public UnionFind(int n) {
            parent = new int[n];
            size = new int[n];
            count = n;
            for (int i = 0; i < n; i++) {
                parent[i] = i;
                size[i] = 1;
            }
        }

        public UnionFind(UnionFind other) {
            this.parent = Arrays.copyOf(other.parent, other.parent.length);
            this.size = Arrays.copyOf(other.size, other.size.length);
            this.count = other.count;
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

    private boolean helper(UnionFind originUf, List<int[]> edges, int k, int w) {
        UnionFind uf = new UnionFind(originUf);
        int idx = 0;
        while (idx < edges.size() && edges.get(idx)[2] >= w) {
            int[] edge = edges.get(idx);
            int u = edge[0], v = edge[1];
            if (uf.union(u, v)) {
                if (uf.count == 1) {
                    return true;
                }
            }
            ++idx;
        }
        w = (w + 1) / 2;
        while (idx < edges.size() && edges.get(idx)[2] >= w && k > 0) {
            int[] edge = edges.get(idx);
            int u = edge[0], v = edge[1];
            if (uf.union(u, v)) {
                if (uf.count == 1) {
                    return true;
                }
                --k;
            }
            ++idx;
        }
        return uf.count == 1;
    }

    public int maxStability(int n, int[][] edges, int k) {
        UnionFind allUf = new UnionFind(n);
        UnionFind uf = new UnionFind(n);
        List<int[]> optionalEdges = new ArrayList<>();
        int right = 200000;
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2], must = edge[3];
            if (must == 1) {
                if (!uf.union(u, v)) {
                    return -1;
                }
                right = Math.min(right, w);
            } else {
                optionalEdges.add(new int[]{u, v, w});
            }
            allUf.union(u, v);
        }
        if (allUf.count > 1) {
            return -1;
        }
        optionalEdges.sort(Comparator.comparingInt(a -> -a[2]));
        int left = 1;
        while (left < right) {
            int mid = left + (right - left + 1) / 2;
            if (helper(uf, optionalEdges, k, mid)) {
                left = mid; // Try for a larger minimum weight
            } else {
                right = mid - 1; // Reduce the search space
            }
        }
        return left;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maxStability(n, edges, k));
    }
}
