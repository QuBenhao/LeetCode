package problems.problems_799;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double champagneTower(int poured, int query_row, int query_glass) {
        double[] dp = new double[]{poured};
        for (int i = 0; i < query_row; i++) {
            double[] nextDp = new double[i + 2];
            for (int j = 0; j <= i; j++) {
                if (dp[j] > 1) {
                    double overflow = (dp[j] - 1) / 2;
                    nextDp[j] += overflow;
                    nextDp[j + 1] += overflow;
                }
            }
            dp = nextDp;
        }
        return Math.min(1.0, dp[query_glass]);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int poured = Integer.parseInt(inputJsonValues[0]);
		int query_row = Integer.parseInt(inputJsonValues[1]);
		int query_glass = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(champagneTower(poured, query_row, query_glass));
    }
}
