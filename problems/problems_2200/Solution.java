package problems.problems_2200;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> findKDistantIndices(int[] nums, int key, int k) {
        List<Integer> result = new ArrayList<>();
        int n = nums.length;
        int last = -1;
        for (int i = 0; i < n; ++i) {
            if (nums[i] != key) {
                continue;
            }
            last = Math.max(last + 1, i - k);
            int end = Math.min(n - 1, i + k);
            for (int j = last; j <= end; ++j) {
                result.add(j);
            }
            last = end;
            if (last >= n - 1) {
                break;
            }
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int key = Integer.parseInt(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(findKDistantIndices(nums, key, k));
    }
}
