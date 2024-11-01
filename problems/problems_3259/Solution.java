package problems.problems_3259;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maxEnergyBoost(int[] a, int[] b) {
        int n = a.length;
        long[][] f = new long[n + 2][2];
        for (int i = 0; i < n; i++) {
            f[i + 2][0] = Math.max(f[i + 1][0], f[i][1]) + a[i];
            f[i + 2][1] = Math.max(f[i + 1][1], f[i][0]) + b[i];
        }
        return Math.max(f[n + 1][0], f[n + 1][1]);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] energyDrinkA = jsonArrayToIntArray(inputJsonValues[0]);
		int[] energyDrinkB = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(maxEnergyBoost(energyDrinkA, energyDrinkB));
    }
}
