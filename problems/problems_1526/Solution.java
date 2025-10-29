package problems.problems_1526;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minNumberOperations(int[] target) {
        // 题目保证答案在 int 范围内
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
