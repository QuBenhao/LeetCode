package problems.problems_3;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int lengthOfLongestSubstring(String s) {
        int ans = 0;
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0, j = -1; i < s.length(); i++) {
            j = Math.max(j, map.getOrDefault(s.charAt(i), -1));
            ans = Math.max(ans, i - j);
            map.put(s.charAt(i), i);
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        String s = values[0];
        return JSON.toJSON(lengthOfLongestSubstring(s));
    }
}
