package problems.problems_LCR_093;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int lenLongestFibSubseq(int[] arr) {
        int n = arr.length;
        Map<Integer, Integer> index = new HashMap<>();
        for (int i = 0; i < n; i++) {
            index.put(arr[i], i);
        }
        Map<Integer, Map<Integer, Integer>> dp = new HashMap<>();
        int ans = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                int nxt = arr[i] + arr[j];
                if (index.containsKey(nxt)) {
                    int k = index.get(nxt);
                    dp.putIfAbsent(j, new HashMap<>());
                    dp.get(j).put(k, dp.getOrDefault(i, new HashMap<>()).getOrDefault(j, 2) + 1);
                    ans = Math.max(ans, dp.get(j).get(k));
                }
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(lenLongestFibSubseq(arr));
    }
}
