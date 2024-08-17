package problems.problems_3137;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumOperationsToMakeKPeriodic(String word, int k) {
        Map<String, Integer> counter = new HashMap<>();
        int n = word.length(), ans = 0;
        for (int i = 0; i < n; i += k) {
            String subString = word.substring(i, i + k);
            counter.put(subString, counter.getOrDefault(subString, 0) + 1);
            ans = Math.max(ans, counter.get(subString));
        }
        return n / k - ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String word = jsonStringToString(inputJsonValues[0]);
        int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minimumOperationsToMakeKPeriodic(word, k));
    }
}
