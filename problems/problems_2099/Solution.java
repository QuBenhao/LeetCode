package problems.problems_2099;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] maxSubsequence(int[] nums, int k) {
        int n = nums.length;
        Integer[] idxes = new Integer[n];
        for (int i = 0; i < n; i++) {
            idxes[i] = i;
        }
        Arrays.sort(idxes, (a, b) -> nums[b] - nums[a]);
        Arrays.sort(idxes, 0, k);
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = nums[idxes[i]];
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxSubsequence(nums, k));
    }
}
