package problems.problems_827;

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

        public int getSize(int x) {
            return size[find(x)];
        }
    }

    private static final int[][] DIRS = new int[][]{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    public int largestIsland(int[][] grid) {
        int n = grid.length;
        int ans = 0;
        UnionFind uf = new UnionFind(n * n);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 0) {
                    continue;
                }
                int p = i * n + j;
                for (int[] dir: DIRS) {
                    int nx = i + dir[0], ny = j + dir[1];
                    if (nx < 0 || nx == n || ny < 0 || ny == n || grid[nx][ny] == 0) {
                        continue;
                    }
                    uf.union(p, nx * n + ny);
                }
                ans = Math.max(ans, uf.getSize(p));
            }
        }
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] != 0) {
                    continue;
                }
                int tot = 1;
                Set<Integer> s = new HashSet<>();
                for (int[] dir: DIRS) {
                    int nx = i + dir[0], ny = j + dir[1];
                    if (nx < 0 || nx == n || ny < 0 || ny == n || grid[nx][ny] == 0) {
                        continue;
                    }
                    int root = uf.find(nx * n + ny);
                    if (s.contains(root)) {
                        continue;
                    }
                    s.add(root);
                    tot += uf.getSize(root);
                }
                ans = Math.max(ans, tot);
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] grid = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(largestIsland(grid));
    }
}
