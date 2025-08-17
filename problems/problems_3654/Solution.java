package problems.problems_3654;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minArraySum(int[] nums, int k) {
        long[] modMin = new long[k];
        Arrays.fill(modMin, Long.MAX_VALUE);
        modMin[0] = 0;
        long cur = 0;
        int mod = 0;
        for (int num : nums) {
            mod = (mod + num) % k;
            cur = Math.min(cur + num, modMin[mod]);
            modMin[mod] = cur;
        }
        return cur;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minArraySum(nums, k));
    }
}
