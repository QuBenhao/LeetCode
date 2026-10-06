package problems.problems_2516;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int takeCharacters(String S, int k) {
        char[] s = S.toCharArray();
        int[] cnt = new int[3];
        for (char c : s) {
            cnt[c - 'a']++; // Initially, take all characters
        }
        if (cnt[0] < k || cnt[1] < k || cnt[2] < k) {
            return -1; // Fewer than k occurrences of a character
        }

        int mx = 0; // Maximum substring length
        int left = 0;
        for (int right = 0; right < s.length; right++) {
            int c = s[right] - 'a';
            cnt[c]--; // Moving c into the window means leaving it untaken
            while (cnt[c] < k) { // Fewer than k occurrences of c remain outside the window
                cnt[s[left] - 'a']++; // Moving s[left] out of the window means taking it
                left++;
            }
            mx = Math.max(mx, right - left + 1);
        }
        return s.length - mx;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(takeCharacters(s, k));
    }
}
