package problems.problems_565;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int arrayNesting(int[] nums) {
        int n = nums.length;
        boolean[] visited = new boolean[n];
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            if (visited[i])
                continue;
            int cur = 1, j = nums[i];
            visited[i] = true;
            while (j != i) {
                visited[j] = true;
                j = nums[j];
                ++cur;
            }
            ans = Math.max(ans, cur);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(arrayNesting(nums));
    }
}
