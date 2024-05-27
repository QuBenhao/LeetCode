package problems.problems_2028;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] missingRolls(int[] rolls, int mean, int n) {
        int remain = mean * (rolls.length + n);
        for (int roll: rolls) {
            remain -= roll;
        }
        if (remain < n || remain > n * 6) {
            return new int[]{};
        }
        int avg = remain / n, extra = remain % n;
        int[] ans = new int[n];
        for (int i = 0; i < n; i++) {
            ans[i] = avg + (i < extra ? 1 : 0);
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int[] rolls = jsonArrayToIntArray(values[0]);
		int mean = Integer.parseInt(values[1]);
		int n = Integer.parseInt(values[2]);
        return JSON.toJSON(missingRolls(rolls, mean, n));
    }
}
