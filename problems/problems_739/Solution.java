package problems.problems_739;

import java.util.Stack;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int[] ans = new int[n];
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            while(!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
                int prev = stack.pop();
                ans[prev] = i - prev;
            }
            stack.add(i);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] temperatures = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(dailyTemperatures(temperatures));
    }
}
