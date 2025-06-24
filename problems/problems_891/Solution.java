package problems.problems_891;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int MOD = 1000000007;
    public int sumSubseqWidths(int[] nums) {
        int n = nums.length;
        Arrays.sort(nums);
        int[] powers = new int[n];
        powers[0] = 1;
        for (int i = 1; i < n; i++) {
            powers[i] = (powers[i - 1] * 2) % MOD;
        }
        long result = 0;
        for (int i = 0; i < n; ++i) {
            result = (result + (long)((powers[i] - powers[n - 1 - i] + MOD) % MOD) * nums[i] % MOD) % MOD;
        }
        return (int) result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(sumSubseqWidths(nums));
    }
}
