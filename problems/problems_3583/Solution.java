package problems.problems_3583;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int MOD = 1_000_000_007;
    public int specialTriplets(int[] nums) {
        Map<Integer, Integer> preCount = new HashMap<>(), sufCount = new HashMap<>();
        for (int num : nums) {
            sufCount.put(num, sufCount.getOrDefault(num, 0) + 1);
        }
        int result = 0;
        for (int num: nums) {
            sufCount.put(num, sufCount.get(num) - 1);
            result = (result + Math.toIntExact((long) preCount.getOrDefault(num * 2, 0) * sufCount.getOrDefault(num * 2, 0) % MOD)) % MOD;
            preCount.put(num, preCount.getOrDefault(num, 0) + 1);
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(specialTriplets(nums));
    }
}
