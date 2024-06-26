package problems.problems_2741;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int specialPerm(int[] nums) {
        int n = nums.length;
        int u = (1 << n) - 1;
        long[][] f = new long[u][n];
        Arrays.fill(f[0], 1L);
        for (int s = 1; s < u; s++) {
            for (int i = 0; i < n; i++) {
                if ((s >> i & 1) != 0) {
                    continue;
                }
                for (int j = 0; j < n; j++) {
                    if ((s >> j & 1) != 0 && (nums[i] % nums[j] == 0 || nums[j] % nums[i] == 0)) {
                        f[s][i] += f[s ^ (1 << j)][j];
                    }
                }
            }
        }
        long ans = 0;
        for (int i = 0; i < n; i++) {
            ans += f[u ^ (1 << i)][i];
        }
        return (int) (ans % 1_000_000_007);
    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(specialPerm(nums));
    }
}
