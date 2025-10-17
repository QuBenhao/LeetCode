package problems.problems_3397;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxDistinctElements(int[] nums, int k) {
        Arrays.sort(nums);
        int ans = 0, cur = Integer.MIN_VALUE;
        for (int num: nums) {
            if (num + k == cur) {
                continue;
            }
            ++ans;
            if (num - k > cur) {
                cur = num - k;
            } else {
                ++cur;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxDistinctElements(nums, k));
    }
}
