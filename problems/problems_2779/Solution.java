package problems.problems_2779;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumBeauty(int[] nums, int k) {
        int m = 0;
        for (int num: nums) {
            m = Math.max(m, num);
        }
        int[] diffs = new int[m + 2];
        for (int num: nums) {
            diffs[Math.max(0, num - k)]++;
            diffs[Math.min(m + 1, num + k + 1)]--;
        }
        int ans = 0, cur = 0;
        for (int v: diffs) {
            cur += v;
            ans = Math.max(ans, cur);
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
		int k = Integer.parseInt(values[1]);
        return JSON.toJSON(maximumBeauty(nums, k));
    }
}
