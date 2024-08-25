package problems.problems_42;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int trap(int[] height) {
        int n = height.length;
        int[] rightMax = new int[n];
        for (int i = n - 2; i >= 0; i--) {
            rightMax[i] = Math.max(rightMax[i + 1], height[i + 1]);
        }
        int ans = 0, leftMax = height[0];
        for (int i = 1; i < n - 1; i++) {
            leftMax = Math.max(leftMax, height[i - 1]);
            int min = Math.min(leftMax, rightMax[i]);
            if (min > height[i]) {
                ans += min - height[i];
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] height = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(trap(height));
    }
}
