package problems.problems_2561;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minCost(int[] basket1, int[] basket2) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int i = 0; i < basket1.length; i++) {
            cnt.merge(basket1[i], 1, Integer::sum);  // cnt[basket1[i]]++
            cnt.merge(basket2[i], -1, Integer::sum); // cnt[basket2[i]]--
        }

        List<Integer> a = new ArrayList<>();
        int mn = Integer.MAX_VALUE;
        for (Map.Entry<Integer, Integer> e : cnt.entrySet()) {
            int x = e.getKey();
            int c = e.getValue();
            if (c % 2 != 0) {
                return -1;
            }
            mn = Math.min(mn, x);
            for (c = Math.abs(c) / 2; c > 0; c--) {
                a.add(x);
            }
        }

        Collections.sort(a);

        long ans = 0;
        for (int i = 0; i < a.size() / 2; i++) {
            ans += Math.min(a.get(i), mn * 2);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] basket1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] basket2 = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minCost(basket1, basket2));
    }
}
