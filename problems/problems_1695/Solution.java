package problems.problems_1695;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumUniqueSubarray(int[] nums) {
        int ans = 0, cur = 0, left = 0;
        Set<Integer> seen = new HashSet<>();
        for (int num: nums) {
            while (seen.contains(num)) {
                seen.remove(nums[left]);
                cur -= nums[left];
                left++;
            }
            seen.add(num);
            cur += num;
            ans = Math.max(ans, cur);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maximumUniqueSubarray(nums));
    }
}
