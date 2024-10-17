package problems.problems_3193;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfPermutations(int n, int[][] requirements) {
        final int MOD = 1_000_000_007;
        int[] req = new int[n];
        Arrays.fill(req, -1);
        req[0] = 0;
        int m = 0;
        for (int[] p : requirements) {
            req[p[0]] = p[1];
            m = Math.max(m, p[1]);
        }
        if (req[0] > 0) {
            return 0;
        }

        int[] f = new int[m + 1];
        f[0] = 1;
        for (int i = 1; i < n; i++) {
            int mx = req[i] < 0 ? m : req[i];
            int r = req[i - 1];
            if (r >= 0) {
                Arrays.fill(f, 0, r, 0);
                Arrays.fill(f, r + 1, Math.min(i + r, mx) + 1, f[r]);
                Arrays.fill(f, Math.min(i + r, mx) + 1, m + 1, 0);
            } else {
                for (int j = 1; j <= mx; j++) { // 计算前缀和
                    f[j] = (f[j] + f[j - 1]) % MOD;
                }
                for (int j = mx; j > i; j--) { // 计算子数组和
                    f[j] = (f[j] - f[j - i - 1] + MOD) % MOD;
                }
            }
        }
        return f[req[n - 1]];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		int[][] requirements = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(numberOfPermutations(n, requirements));
    }
}
