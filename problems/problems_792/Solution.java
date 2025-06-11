package problems.problems_792;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numMatchingSubseq(String s, String[] words) {
        Map<Character, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < s.length(); ++i) {
            char c = s.charAt(i);
            map.putIfAbsent(c, new ArrayList<>());
            map.get(c).add(i);
        }
        int ans = 0;
        for (String word: words) {
            int idx = 0, m = word.length();
            int sIdx = -1;
            while (idx < m) {
                char c = word.charAt(idx);
                if (!map.containsKey(c)) {
                    break;
                }
                List<Integer> list = map.get(c);
                int l = 0, r = list.size();
                while (l < r) {
                    int mid = l + (r - l) / 2;
                    if (list.get(mid) < sIdx + 1) {
                        l = mid + 1;
                    } else {
                        r = mid;
                    }
                }
                if (l == list.size()) {
                    break;
                }
                sIdx = list.get(l);
                ++idx;
            }
            ans += (idx == m) ? 1 : 0;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		String[] words = jsonArrayToStringArray(inputJsonValues[1]);
        return JSON.toJSON(numMatchingSubseq(s, words));
    }
}
