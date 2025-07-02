package problems.problems_904;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int totalFruit(int[] fruits) {
        int ans = 0;
        int left = 0;
        int n = fruits.length;
        Map<Integer, Integer> count = new HashMap<>(3);
        for (int right = 0; right < n; right++) {
            count.put(fruits[right], count.getOrDefault(fruits[right], 0) + 1);
            while (count.size() > 2) {
                count.put(fruits[left], count.get(fruits[left]) - 1);
                if (count.get(fruits[left]) == 0) {
                    count.remove(fruits[left]);
                }
                left++;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] fruits = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(totalFruit(fruits));
    }
}
