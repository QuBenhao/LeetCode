package problems.problems_3185;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long countCompleteDayPairs(int[] hours) {
        long[] hs = new long[24];
        for (int h : hours) {
            hs[h % 24]++;
        }
        long ans = 0;
        for (int i = 1; i < 12; i++) {
            ans += hs[i] * hs[24 - i];
        }
        ans += hs[0] * (hs[0] - 1) / 2;
        ans += hs[12] * (hs[12] - 1) / 2;
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] hours = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(countCompleteDayPairs(hours));
    }
}
