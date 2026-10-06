package problems.problems_2376;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countSpecialNumbers(int n) {
        char[] s = Integer.toString(n).toCharArray();
        int[][] memo = new int[s.length][1 << 10];
        for (int[] row : memo) {
            Arrays.fill(row, -1); // -1 means not yet computed
        }
        return dfs(0, 0, true, false, s, memo);
    }

    private int dfs(int i, int mask, boolean isLimit, boolean isNum, char[] s, int[][] memo) {
        if (i == s.length) {
            return isNum ? 1 : 0; // isNum being true means a valid number has been formed
        }
        if (!isLimit && isNum && memo[i][mask] != -1) {
            return memo[i][mask]; // Already computed
        }
        int res = 0;
        if (!isNum) { // The current digit can be skipped
            res = dfs(i + 1, mask, false, false, s, memo);
        }
        // If all previous digits match n, this digit can be at most s[i] (otherwise the number would exceed n)
        int up = isLimit ? s[i] - '0' : 9;
        // Enumerate the digit d to place
        // If no digit has been placed, start at 1 to avoid leading zeros
        for (int d = isNum ? 0 : 1; d <= up; d++) {
            if ((mask >> d & 1) == 0) { // If d is absent from mask, it has not been used before
                res += dfs(i + 1, mask | (1 << d), isLimit && d == up, true, s, memo);
            }
        }
        if (!isLimit && isNum) {
            memo[i][mask] = res; // Memoization
        }
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(countSpecialNumbers(n));
    }
}
