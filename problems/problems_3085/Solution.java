package problems.problems_3085;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumDeletions(String word, int k) {
        int[] count = new int[26];
        for (char c : word.toCharArray()) {
            count[c - 'a']++;
        }
        Arrays.sort(count);
        int ans = word.length();
        for (int i = 0; i < 26; ++i) {
            if (i > 0 && count[i] == count[i - 1]) continue;
            int cur = 0, maxV = count[i] + k;
            for (int j = 0; j < i; ++j) {
                if (count[j] >= count[i]) {
                    break;
                }
                cur += count[j];
            }
            for (int j = 25; j > i; --j) {
                if (count[j] <= maxV) {
                    break;
                }
                cur += count[j] - maxV;
            }
            ans = Math.min(ans, cur);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String word = jsonStringToString(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minimumDeletions(word, k));
    }
}
