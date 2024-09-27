package problems.problems_2516;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int takeCharacters(String S, int k) {
        char[] s = S.toCharArray();
        int[] cnt = new int[3];
        for (char c : s) {
            cnt[c - 'a']++; // 一开始，把所有字母都取走
        }
        if (cnt[0] < k || cnt[1] < k || cnt[2] < k) {
            return -1; // 字母个数不足 k
        }

        int mx = 0; // 子串最大长度
        int left = 0;
        for (int right = 0; right < s.length; right++) {
            int c = s[right] - 'a';
            cnt[c]--; // 移入窗口，相当于不取走 c
            while (cnt[c] < k) { // 窗口之外的 c 不足 k
                cnt[s[left] - 'a']++; // 移出窗口，相当于取走 s[left]
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
