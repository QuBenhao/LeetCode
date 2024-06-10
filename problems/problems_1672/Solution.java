package problems.problems_1672;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumWealth(int[][] accounts) {
        int ans = 0;
        for (int[] account : accounts) {
            int s = 0;
            for (int a : account) {
                s += a;
            }
            ans = Math.max(ans, s);
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int[][] accounts = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(maximumWealth(accounts));
    }
}
