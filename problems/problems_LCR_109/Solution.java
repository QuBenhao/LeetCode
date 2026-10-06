package problems.problems_LCR_109;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    String t, s;
    Set<String> set = new HashSet<>();
    public int openLock(String[] _ds, String _t) {
        s = "0000";
        t = _t;
        if (s.equals(t)) return 0;
        set.addAll(Arrays.asList(_ds));
        if (set.contains(s)) return -1;
        return bfs();
    }
    int bfs() {
        // d1 searches forward from s
        // d2 searches backward from t
        Deque<String> d1 = new ArrayDeque<>(), d2 = new ArrayDeque<>();
        /*
         * m1 and m2 record how many transformations reach each state from their respective directions
         * e.g.
         * m1 = {"1000":1} means "1000" is reached from s="0000" in one turn
         * m2 = {"9999":3} means "9999" is reached from t="9996" in three turns
         */
        Map<String, Integer> m1 = new HashMap<>(), m2 = new HashMap<>();
        d1.addLast(s);
        m1.put(s, 0);
        d2.addLast(t);
        m2.put(t, 0);

        /*
         * Continue searching only while both queues are nonempty
         * If either queue is empty, the search in that direction has exhausted all possibilities without reaching its target
         * e.g.
         * For example, if d1 is empty, searching from s could not reach t, so continuing the reverse search is unnecessary
         */
        while (!d1.isEmpty() && !d2.isEmpty()) {
            int t = -1;
            if (d1.size() <= d2.size()) {
                t = update(d1, m1, m2);
            } else {
                t = update(d2, m2, m1);
            }
            if (t != -1) return t;
        }
        return -1;
    }
    int update(Deque<String> deque, Map<String, Integer> cur, Map<String, Integer> other) {
        int m = deque.size();
        while (m-- > 0) {
            String poll = deque.pollFirst();
            if (poll == null) continue;
            char[] pcs = poll.toCharArray();
            int step = cur.get(poll);
            // Enumerate the character to replace
            for (int i = 0; i < 4; i++) {
                // A wheel can turn forward or backward; enumerate offsets [-1,1] and skip 0
                for (int j = -1; j <= 1; j++) {
                    if (j == 0) continue;

                    // Construct the replacement string str
                    int origin = pcs[i] - '0';
                    int next = (origin + j) % 10;
                    if (next == -1) next = 9;

                    char[] clone = pcs.clone();
                    clone[i] = (char)(next + '0');
                    String str = String.valueOf(clone);

                    if (set.contains(str)) continue;
                    if (cur.containsKey(str)) continue;

                    // If the opposite direction has reached it, the shortest path is found; otherwise, enqueue it
                    if (other.containsKey(str)) {
                        return step + 1 + other.get(str);
                    } else {
                        deque.addLast(str);
                        cur.put(str, step + 1);
                    }
                }
            }
        }
        return -1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] deadends = jsonArrayToStringArray(inputJsonValues[0]);
		String target = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(openLock(deadends, target));
    }
}
