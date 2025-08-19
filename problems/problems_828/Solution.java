package problems.problems_828;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int uniqueLetterString(String s) {
        int n = s.length();
        Map<Character, List<Integer>> charIndices = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            charIndices.computeIfAbsent(s.charAt(i), k -> new ArrayList<>()).add(i);
        }
        int ans = 0;
        for (List<Integer> indices : charIndices.values()) {
            int m = indices.size();
            if (m == 0) {
                continue;
            }
            if (m == 1) {
                ans += (indices.get(0) + 1) * (n - indices.get(0));
                continue;
            }
            int last = indices.get(0) + 1;
            for (int i = 0; i < m; ++i) {
                int cur = (i == m - 1 ? n : indices.get(i + 1)) - indices.get(i);
                ans += last * cur;
                last = cur;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(uniqueLetterString(s));
    }
}
