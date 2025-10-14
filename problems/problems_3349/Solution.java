package problems.problems_3349;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
        int a = 0, b = k;
        int n = nums.size() - k;
        out:
        while (b <= n) {
            for (int j = a + 1; j < b; ++j) {
                if (nums.get(j) <= nums.get(j - 1)) {
                    b += j - a;
                    a += j - a;
                    continue out;
                }
            }
            for (int j = b + 1; j < b + k; ++j) {
                if (nums.get(j) <= nums.get(j - 1)) {
                    a += j - b;
                    b += j - b;
                    continue out;
                }
            }
            return true;
        }
        return false;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<Integer> nums = jsonArrayToIntList(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(hasIncreasingSubarrays(nums, k));
    }
}
