package problems.problems_3186;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maximumTotalDamage(int[] power) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int p: power) {
            map.put(p, map.getOrDefault(p, 0) + 1);
        }
        int n = map.size();
        long[] dp = new long[n + 1];
        List<Integer> keys = new ArrayList<Integer>(map.keySet());
        Collections.sort(keys);
        for (int i = 1, j = 0; i <= n; i++) {
            int currPower = keys.get(i - 1);
            while (keys.get(j) < currPower - 2) {
                j++;
            }
            dp[i] = Math.max(dp[i - 1], dp[j] + (long) currPower * map.get(currPower));
        }
        return dp[n];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] power = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maximumTotalDamage(power));
    }
}
