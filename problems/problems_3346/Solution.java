package problems.problems_3346;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxFrequency(int[] nums, int k, int numOperations) {
        Map<Integer, Integer> cnt = new HashMap<>();
        Map<Integer, Integer> diff = new TreeMap<>();
        for (int x : nums) {
            cnt.merge(x, 1, Integer::sum); // cnt[x]++
            diff.putIfAbsent(x, 0); // 把 x 插入 diff，以保证下面能遍历到 x
            // 把 [x-k, x+k] 中的每个整数的出现次数都加一
            diff.merge(x - k, 1, Integer::sum); // diff[x-k]++
            diff.merge(x + k + 1, -1, Integer::sum); // diff[x+k+1]--
        }

        int ans = 0;
        int sumD = 0;
        for (Map.Entry<Integer, Integer> e : diff.entrySet()) {
            sumD += e.getValue();
            ans = Math.max(ans, Math.min(sumD, cnt.getOrDefault(e.getKey(), 0) + numOperations));
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int numOperations = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maxFrequency(nums, k, numOperations));
    }
}
