package problems.problems_3618;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int MAX_N = 100000;
    private static final boolean[] FLAG = new boolean[MAX_N + 1];
    static {
        FLAG[0] = true;
        FLAG[1] = true;
        for (int i = 2; i * i <= MAX_N; i++) {
            if (!FLAG[i]) {
                for (int j = i * 2; j <= MAX_N; j += i) {
                    FLAG[j] = true;
                }
            }
        }
    }

    public long splitArray(int[] nums) {
        long ans = 0;
        for (int i = 0; i < nums.length; i++) {
            if (FLAG[i]) {
                ans += nums[i];
            } else {
                ans -= nums[i];
            }
        }
        return Math.abs(ans);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(splitArray(nums));
    }
}
