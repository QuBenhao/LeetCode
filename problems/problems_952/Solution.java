package problems.problems_952;

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
    private static final int MAX_N = 100000;
    private static List<Integer>[] PRIMES = new List[MAX_N + 1];
    static {
        for (int i = 0; i <= MAX_N; ++i) {
            PRIMES[i] = new ArrayList<>();
        }
        for (int i = 2; i <= MAX_N; ++i) {
            if (PRIMES[i].isEmpty()) {
                for (int j = i; j <= MAX_N; j += i) {
                    PRIMES[j].add(i);
                }
            }
        }
    }
    public int largestComponentSize(int[] nums) {
        int n = nums.length;
        UnionFind uf = new UnionFind(n);
        Map<Integer, Integer> primeIdx = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            for (int p: PRIMES[nums[i]]) {
                if (primeIdx.containsKey(p)) {
                    uf.union(primeIdx.get(p), i);
                }
                primeIdx.put(p, i);
            }
        }
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = Math.max(ans, uf.getSize(i));
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(largestComponentSize(nums));
    }
}
