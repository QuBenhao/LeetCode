package problems.problems_438;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int helper(int[] counts, int key, int val) {
        boolean before = counts[key] == 0;
        counts[key] += val;
        if (before) {
            return 1;
        }
        if (counts[key] == 0) {
            return -1;
        }
        return 0;
    }
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> ans = new ArrayList<>();
        int[] counts = new int[26];
        Arrays.fill(counts, 0);
        int m = s.length(), n = p.length();
        for (int i = 0; i < n; i++) {
            counts[p.charAt(i) - 'a']--;
        }
        int diff = 0;
        for (int i = 0; i < 26; i++) {
            if (counts[i] != 0) {
                diff++;
            }
        }
        for (int i = 0; i < m; i++) {
            diff += helper(counts, s.charAt(i) - 'a', 1);
            if (i >= n - 1) {
                if (diff == 0) {
                    ans.add(i - n + 1);
                }
                diff += helper(counts, s.charAt(i - n + 1) - 'a', -1);
            }
        }
        return ans;
    }



    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		String p = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(findAnagrams(s, p));
    }
}
