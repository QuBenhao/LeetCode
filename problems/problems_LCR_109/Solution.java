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
        // d1 代表从起点 s 开始搜索（正向）
        // d2 代表从结尾 t 开始搜索（反向）
        Deque<String> d1 = new ArrayDeque<>(), d2 = new ArrayDeque<>();
        /*
         * m1 和 m2 分别记录两个方向出现的状态是经过多少次转换而来
         * e.g.
         * m1 = {"1000":1} 代表 "1000" 由 s="0000" 旋转 1 次而来
         * m2 = {"9999":3} 代表 "9999" 由 t="9996" 旋转 3 次而来
         */
        Map<String, Integer> m1 = new HashMap<>(), m2 = new HashMap<>();
        d1.addLast(s);
        m1.put(s, 0);
        d2.addLast(t);
        m2.put(t, 0);

        /*
         * 只有两个队列都不空，才有必要继续往下搜索
         * 如果其中一个队列空了，说明从某个方向搜到底都搜不到该方向的目标节点
         * e.g.
         * 例如，如果 d1 为空了，说明从 s 搜索到底都搜索不到 t，反向搜索也没必要进行了
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
            // 枚举替换哪个字符
            for (int i = 0; i < 4; i++) {
                // 能「正向转」也能「反向转」，这里直接枚举偏移量 [-1,1] 然后跳过 0
                for (int j = -1; j <= 1; j++) {
                    if (j == 0) continue;

                    // 求得替换字符串 str
                    int origin = pcs[i] - '0';
                    int next = (origin + j) % 10;
                    if (next == -1) next = 9;

                    char[] clone = pcs.clone();
                    clone[i] = (char)(next + '0');
                    String str = String.valueOf(clone);

                    if (set.contains(str)) continue;
                    if (cur.containsKey(str)) continue;

                    // 如果在「另一方向」找到过，说明找到了最短路，否则加入队列
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
