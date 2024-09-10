package problems.problems_2552;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long countQuadruplets(int[] nums) {
        long cnt4 = 0;
        int n = nums.length;
        long[] cnt3 = new long[n];
        for (int l = 2; l < n; l++) {
            long cnt2 = 0;
            for (int j = 0; j < l; j++) {
                if (nums[j] < nums[l]) {
                    cnt4 += cnt3[j];
                    cnt2++;
                } else {
                    cnt3[j] += cnt2;
                }
            }
        }
        return cnt4;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(countQuadruplets(nums));
    }
}
