package problems.problems_1542;

import com.alibaba.fastjson.JSON;
import qubhjava.BaseSolution;

import java.util.Arrays;


public class Solution extends BaseSolution {
    private static final int D = 10; // Number of possible distinct characters in s

    public int longestAwesome(String s) {
        int n = s.length();
        int[] pos = new int[1 << D];
        Arrays.fill(pos, n); // n means this prefix XOR has not been found
        pos[0] = -1; // pre[-1] = 0
        int ans = 0;
        int pre = 0;
        for (int i = 0; i < n; i++) {
            pre ^= 1 << (s.charAt(i) - '0');
            for (int d = 0; d < D; d++) {
                ans = Math.max(ans, i - pos[pre ^ (1 << d)]); // Odd count
            }
            ans = Math.max(ans, i - pos[pre]); // Even count
            if (pos[pre] == n) { // Record index i on the first occurrence of prefix XOR pre
                pos[pre] = i;
            }
        }
        return ans;
    }


    @Override
    public Object solve(String[] values) {
        String s = values[0];
        return JSON.toJSON(longestAwesome(s));
    }
}
