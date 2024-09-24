package problems.problems_2207;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maximumSubsequenceCount(String text, String pattern) {
        long ans = 0, p0 = 0, p1 = 0;
        char c0 = pattern.charAt(0), c1 = pattern.charAt(1);
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (c == c1) {
                ans += p0;
                p1++;
            } 
            if (c == c0) {
                p0++;
            }
        }
        return ans + Math.max(p0, p1);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String text = jsonStringToString(inputJsonValues[0]);
		String pattern = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(maximumSubsequenceCount(text, pattern));
    }
}
