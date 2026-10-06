package problems.problems_1526;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minNumberOperations(int[] target) {
        // The problem guarantees that the answer fits in int
        int ans = target[0];
        for (int i = 1; i < target.length; i++) {
            ans += Math.max(target[i] - target[i - 1], 0);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] target = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(minNumberOperations(target));
    }
}
