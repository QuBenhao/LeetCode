package problems.problems_11;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxArea(int[] height) {
        int ans = 0;
        for (int i = 0, j = height.length - 1; i < j; ) {
            ans = Math.max(ans, Math.min(height[i], height[j]) * (j - i));
            if (height[i] > height[j]) {
                j--;
            } else {
                i++;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int[] height = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(maxArea(height));
    }
}
