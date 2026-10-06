package problems.problems_LCR_108;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    String s, e;
    Set<String> set = new HashSet<>();
    public int ladderLength(String _s, String _e, List<String> ws) {
        set.clear();
        s = _s;
        e = _e;
        // Put all words in set; if the target word is absent, there is no solution
        set.addAll(ws);
        if (!set.contains(e)) return 0;
        int ans = bfs();
        return ans == -1 ? 0 : ans + 1;
    }

    int bfs() {
        // d1 searches forward from beginWord
        // d2 searches backward from endWord
        Deque<String> d1 = new ArrayDeque<>(), d2 = new ArrayDeque<>();

        /*
         * m1 and m2 record how many transformations reach each word from their respective directions
         * e.g.
         * m1 = {"abc":1} means abc is reached from beginWord by replacing one character
         * m2 = {"xyz":3} means xyz is reached from endWord by replacing three characters
         */
        Map<String, Integer> m1 = new HashMap<>(), m2 = new HashMap<>();
        d1.add(s);
        m1.put(s, 0);
        d2.add(e);
        m2.put(e, 0);

        /*
         * Continue searching only while both queues are nonempty
         * If either queue is empty, the search in that direction has exhausted all possibilities without reaching its target
         * e.g.
         * For example, if d1 is empty, searching from beginWord could not reach endWord, so continuing the reverse search is unnecessary
         */
        while (!d1.isEmpty() && !d2.isEmpty()) {
            int t;
            // Expand the direction with fewer queued elements first to keep the two searches as balanced as possible
            if (d1.size() <= d2.size()) {
                t = update(d1, m1, m2);
            } else {
                t = update(d2, m2, m1);
            }
            if (t != -1) return t;
        }
        return -1;
    }

    // update expands words taken from deque,
    // cur stores distances in the current direction; other stores distances in the opposite direction
    int update(Deque<String> deque, Map<String, Integer> cur, Map<String, Integer> other) {
        int m = deque.size();
        while (m-- > 0) {
            // Get the original string to expand
            String poll = deque.pollFirst();
            int n = poll.length();

            // Enumerate the character position i to replace in the original string
            for (int i = 0; i < n; i++) {
                // Enumerate which lowercase letter replaces position i
                for (int j = 0; j < 26; j++) {
                    // String after replacement
                    String sub = poll.substring(0, i) + String.valueOf((char)('a' + j)) + poll.substring(i + 1);
                    if (set.contains(sub)) {
                        // Skip the string if it has already been recorded (expanded) in the current direction
                        if (cur.containsKey(sub) && cur.get(sub) <= cur.get(poll) + 1) continue;

                        // If the string was reached from the opposite direction, the shortest path connecting the searches has been found
                        if (other.containsKey(sub)) {
                            return cur.get(poll) + 1 + other.get(sub);
                        } else {
                            // Otherwise, add it to deque
                            deque.addLast(sub);
                            cur.put(sub, cur.get(poll) + 1);
                        }
                    }
                }
            }
        }
        return -1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String beginWord = jsonStringToString(inputJsonValues[0]);
		String endWord = jsonStringToString(inputJsonValues[1]);
		List<String> wordList = jsonArrayToStringList(inputJsonValues[2]);
        return JSON.toJSON(ladderLength(beginWord, endWord, wordList));
    }
}
