package problems.problems_84;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int largestRectangleArea(int[] heights) {
        Deque<Integer> stack = new ArrayDeque<>();
        int n = heights.length;
        stack.addLast(-1);
        int ans = 0;
        for (int i = 0; i <= n; i++) {
            int h = i == n ? 0 : heights[i];
            while (stack.peekLast() != -1 && heights[stack.peekLast()] >= h) {
                ans = Math.max(ans, heights[stack.pollLast()] * (i - stack.peekLast() - 1));
            }
            stack.addLast(i);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] heights = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(largestRectangleArea(heights));
    }
}
