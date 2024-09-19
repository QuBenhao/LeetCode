package problems.problems_LCR_038;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] ans = new int[n];
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            while (!stack.isEmpty() && temperatures[i] > temperatures[stack.peek()]) {
                int preIndex = stack.pop();
                ans[preIndex] = i - preIndex;
            }
            stack.push(i);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] temperatures = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(dailyTemperatures(temperatures));
    }
}
