package problems.problems_LCR_015;

import java.util.ArrayList;
import java.util.List;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] count = new int[26];
        int diff = 0;
        int n = p.length();
        for (int i = 0; i < n; i++) {
            if (count[p.charAt(i) - 'a']++ == 0) {
                diff++;
            }
        }
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            count[c - 'a']--;
            if (count[c - 'a'] == 0) {
                diff--;
            } else if (count[c - 'a'] == -1) {
                diff++;
            }
            if (i >= n - 1) {
                if (diff == 0) {
                    ans.add(i - n + 1);
                }
                char old = s.charAt(i - n + 1);
                count[old - 'a']++;
                if (count[old - 'a'] == 0) {
                    diff--;
                } else if (count[old - 'a'] == 1) {
                    diff++;
                }
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
