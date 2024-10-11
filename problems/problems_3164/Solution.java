package problems.problems_3164;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long numberOfPairs(int[] nums1, int[] nums2, int k) {
        Map<Integer, Integer> cnt1 = new HashMap<>();
        for (int x : nums1) {
            if (x % k == 0) {
                cnt1.merge(x / k, 1, Integer::sum); // cnt1[x/k]++
            }
        }
        if (cnt1.isEmpty()) {
            return 0;
        }

        Map<Integer, Integer> cnt2 = new HashMap<>();
        for (int x : nums2) {
            cnt2.merge(x, 1, Integer::sum); // cnt2[x]++
        }

        long ans = 0;
        int u = Collections.max(cnt1.keySet());
        for (Map.Entry<Integer, Integer> e : cnt2.entrySet()) {
            int x = e.getKey();
            int cnt = e.getValue();
            int s = 0;
            for (int y = x; y <= u; y += x) { // 枚举 x 的倍数
                if (cnt1.containsKey(y)) {
                    s += cnt1.get(y);
                }
            }
            ans += (long) s * cnt;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] nums2 = jsonArrayToIntArray(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(numberOfPairs(nums1, nums2, k));
    }
}
