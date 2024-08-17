package problems.problems_LCR_014;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean checkInclusion(String s1, String s2) {
        int[] cnt1 = new int[26], cnt2 = new int[26];
        int m = s1.length(), n = s2.length();
        for (int i = 0; i < m; i++) {
            cnt1[s1.charAt(i) - 'a']++;
        }
        for (int i = 0; i < n; i++) {
            cnt2[s2.charAt(i) - 'a']++;
            if (i >= m - 1) {
                if (Arrays.equals(cnt1, cnt2)) {
                    return true;
                }
                cnt2[s2.charAt(i - m + 1) - 'a']--;
            }
        }
        return false;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s1 = jsonStringToString(inputJsonValues[0]);
		String s2 = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(checkInclusion(s1, s2));
    }
}
