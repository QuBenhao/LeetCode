package problems.problems_3445;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxDifference(String s, int k) {
        int ans = Integer.MIN_VALUE;
        for (int x = 0; x < 5; ++x) {
            for (int y = 0; y < 5; ++y) {
                if (x == y) continue;
                int[] curSum = new int[5];
                int[] prevSum = new int[5];
                int[][] minS = new int[][]{{Integer.MAX_VALUE>>2, Integer.MAX_VALUE>>2}, {Integer.MAX_VALUE>>2, Integer.MAX_VALUE>>2}};
                for (int left = 0, right = 0; right < s.length(); ++right) {
                    ++curSum[s.charAt(right) - '0'];
                    while (right - left + 1 >= k && curSum[x] > prevSum[x] && curSum[y] > prevSum[y]) {
                        int p = prevSum[x] & 1, q = prevSum[y] & 1;
                        minS[p][q] = Math.min(minS[p][q], prevSum[x] - prevSum[y]);
                        ++prevSum[s.charAt(left) - '0'];
                        ++left;
                    }
                    if (right + 1 >= k) {
                        ans = Math.max(ans, curSum[x] - curSum[y] - minS[curSum[x] & 1 ^ 1][curSum[y] & 1]);
                    }
                }
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxDifference(s, k));
    }
}
