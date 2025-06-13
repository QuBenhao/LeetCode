package problems.problems_3533;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private boolean dfs(int[] nums, int[] pow10, int[] ans, int idx, int n, int k, int s, int x, List<Map<Integer, Boolean>> cache) {
        Map<Integer, Boolean> map = cache.get(x);
        if (map.containsKey(s)) {
            return map.get(s);
        }
        if (s == 0) {
            boolean res = x % k == 0;
            map.put(s, res);
            return res;
        }
        for (int i = 0; i < n; ++i) {
            if (((s >> i) & 1) == 0) {
                continue;
            }
            int nextS = s ^ (1 << i);
            int nextX = (x * pow10[i] + nums[i]) % k;
            if (dfs(nums, pow10, ans, idx+1, n, k, nextS, nextX, cache)) {
                ans[idx] = nums[i];
                map.put(s, true);
                return true;
            }
        }
        map.put(s, false);
        return false;
    }

    public int[] concatenatedDivisibility(int[] nums, int k) {
        int n = nums.length;
        Arrays.sort(nums);
        int[] result = new int[n];
        int[] pow10 = new int[n];
        int mask = 1 << n;
        List<Map<Integer, Boolean>> cache = new ArrayList<>(k);
        for (int i = 0; i < k; ++i) {
            cache.add(new HashMap<>(mask));
        }
        for (int i = 0; i < n; ++i) {
            pow10[i] = 1;
            for (int num = nums[i]; num > 0; num /= 10) {
                pow10[i] = (pow10[i] * 10) % k;
            }
        }
        if (dfs(nums, pow10, result, 0, n, k, mask-1, 0, cache)) {
            return result;
        }
        return new int[]{};
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(concatenatedDivisibility(nums, k));
    }
}
