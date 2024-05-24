package problems.problems_1673;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] mostCompetitive(int[] nums, int k) {
        int[] ans = new int[k];
        for (int i = 0, idx = -1, n = nums.length; i < n; i++) {
            while (idx >= 0 && nums[i] < ans[idx] && idx + 1 + n - i > k) {
                idx--;
            }
            if (idx < k - 1) {
                ans[++idx] = nums[i];
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
		int k = Integer.parseInt(values[1]);
        return JSON.toJSON(mostCompetitive(nums, k));
    }
}
