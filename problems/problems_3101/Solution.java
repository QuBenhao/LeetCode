package problems.problems_3101;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long countAlternatingSubarrays(int[] nums) {
        long ans = 0L, cnt = 0L;
        for (int i = 0; i < nums.length; i++) {
            if (i == 0 || nums[i] != nums[i - 1]) {
                cnt++;
            } else {
                cnt = 1;
            }
            ans += cnt;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(countAlternatingSubarrays(nums));
    }
}
