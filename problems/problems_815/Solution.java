package problems.problems_815;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    static int N = (int)1e6+10;
    static int[] p = new int[N];
    int find(int x) {
        if (p[x] != x) p[x] = find(p[x]);
        return p[x];
    }
    void union(int a, int b) {
        p[find(a)] = p[find(b)];
    }
    boolean query(int a, int b) {
        return find(a) == find(b);
    }
    int s, t;
    int[][] rs;
    public int numBusesToDestination(int[][] _rs, int _s, int _t) {
        rs = _rs; s = _s; t = _t;
        if (s == t) return 0;
        for (int i = 0; i < N; i++) p[i] = i;
        for (int[] r : rs) {
            for (int loc : r) {
                union(loc, r[0]);
            }
        }
        if (!query(s, t)) return -1;
        int ans = bfs();
        return ans;
    }
    // Record the routes accessible from each stop
    Map<Integer, Set<Integer>> map = new HashMap<>();
    int bfs() {
        Deque<Integer> d1 = new ArrayDeque<>(), d2 = new ArrayDeque<>();
        Map<Integer, Integer> m1 = new HashMap<>(), m2 = new HashMap<>();

        int n = rs.length;
        for (int i = 0; i < n; i++) {
            for (int station : rs[i]) {
                // Add routes accessible from the source to the forward queue
                if (station == s) {
                    d1.addLast(i);
                    m1.put(i, 1);
                }
                // Add routes accessible from the destination to the backward queue
                if (station == t) {
                    d2.addLast(i);
                    m2.put(i, 1);
                }
                Set<Integer> set = map.getOrDefault(station, new HashSet<>());
                set.add(i);
                map.put(station, set);
            }
        }

        // If the source and destination share an accessible route, return 1 immediately
        Set<Integer> s1 = map.get(s), s2 = map.get(t);
        Set<Integer> tot = new HashSet<>(s1);
        tot.retainAll(s2);
        if (!tot.isEmpty()) return 1;

        // Bidirectional BFS
        while (!d1.isEmpty() && !d2.isEmpty()) {
            int res = -1;
            if (d1.size() <= d2.size()) {
                res = update(d1, m1, m2);
            } else {
                res = update(d2, m2, m1);
            }
            if (res != -1) return res;
        }

        return 0x3f3f3f3f; // never
    }
    int update(Deque<Integer> d, Map<Integer, Integer> cur, Map<Integer, Integer> other) {
        int m = d.size();
        while (m-- > 0) {
            // Pop the current route and the distance needed to reach it
            int poll = !d.isEmpty() ? d.pollFirst() : -1;
            int step = cur.get(poll);

            // Iterate over the stops on this route
            for (int station : rs[poll]) {
                // Iterate over routes accessible from this route's stops
                Set<Integer> lines = map.get(station);
                if (lines == null) continue;
                for (int nr : lines) {
                    if (cur.containsKey(nr)) continue;
                    if (other.containsKey(nr)) return step + other.get(nr);
                    cur.put(nr, step + 1);
                    d.add(nr);
                }
            }
        }
        return -1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] routes = jsonArrayToInt2DArray(inputJsonValues[0]);
		int source = Integer.parseInt(inputJsonValues[1]);
		int target = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(numBusesToDestination(routes, source, target));
    }
}
