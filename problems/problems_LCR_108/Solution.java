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
        // 将所有 word 存入 set，如果目标单词不在 set 中，说明无解
        set.addAll(ws);
        if (!set.contains(e)) return 0;
        int ans = bfs();
        return ans == -1 ? 0 : ans + 1;
    }

    int bfs() {
        // d1 代表从起点 beginWord 开始搜索（正向）
        // d2 代表从结尾 endWord 开始搜索（反向）
        Deque<String> d1 = new ArrayDeque<>(), d2 = new ArrayDeque<>();

        /*
         * m1 和 m2 分别记录两个方向出现的单词是经过多少次转换而来
         * e.g.
         * m1 = {"abc":1} 代表 abc 由 beginWord 替换 1 次字符而来
         * m2 = {"xyz":3} 代表 xyz 由 endWord 替换 3 次字符而来
         */
        Map<String, Integer> m1 = new HashMap<>(), m2 = new HashMap<>();
        d1.add(s);
        m1.put(s, 0);
        d2.add(e);
        m2.put(e, 0);

        /*
         * 只有两个队列都不空，才有必要继续往下搜索
         * 如果其中一个队列空了，说明从某个方向搜到底都搜不到该方向的目标节点
         * e.g.
         * 例如，如果 d1 为空了，说明从 beginWord 搜索到底都搜索不到 endWord，反向搜索也没必要进行了
         */
        while (!d1.isEmpty() && !d2.isEmpty()) {
            int t;
            // 为了让两个方向的搜索尽可能平均，优先拓展队列内元素少的方向
            if (d1.size() <= d2.size()) {
                t = update(d1, m1, m2);
            } else {
                t = update(d2, m2, m1);
            }
            if (t != -1) return t;
        }
        return -1;
    }

    // update 代表从 deque 中取出一个单词进行扩展，
    // cur 为当前方向的距离字典；other 为另外一个方向的距离字典
    int update(Deque<String> deque, Map<String, Integer> cur, Map<String, Integer> other) {
        int m = deque.size();
        while (m-- > 0) {
            // 获取当前需要扩展的原字符串
            String poll = deque.pollFirst();
            int n = poll.length();

            // 枚举替换原字符串的哪个字符 i
            for (int i = 0; i < n; i++) {
                // 枚举将 i 替换成哪个小写字母
                for (int j = 0; j < 26; j++) {
                    // 替换后的字符串
                    String sub = poll.substring(0, i) + String.valueOf((char)('a' + j)) + poll.substring(i + 1);
                    if (set.contains(sub)) {
                        // 如果该字符串在「当前方向」被记录过（拓展过），跳过即可
                        if (cur.containsKey(sub) && cur.get(sub) <= cur.get(poll) + 1) continue;

                        // 如果该字符串在「另一方向」出现过，说明找到了联通两个方向的最短路
                        if (other.containsKey(sub)) {
                            return cur.get(poll) + 1 + other.get(sub);
                        } else {
                            // 否则加入 deque 队列
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
