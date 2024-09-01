package problems.problems_2024;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        int n = answerKey.length();
        int countT = 0;
        int ans = 0;
        for (int l = 0, r = 0; r < n; r++) {
            if (answerKey.charAt(r) == 'T') {
                countT++;
            }
            while (countT > k && r - l + 1 - countT > k) {
                if (answerKey.charAt(l) == 'T') {
                    countT--;
                }
                l++;
            }
            ans = Math.max(ans, r - l + 1);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String answerKey = jsonStringToString(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxConsecutiveAnswers(answerKey, k));
    }
}
