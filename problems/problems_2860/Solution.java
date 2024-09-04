package problems.problems_2860;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countWays(List<Integer> nums) {
        Collections.sort(nums);
        int n = nums.size();
        int ans = nums.getFirst() > 0 ? 2 : 1;
        for (int i = 1; i < n; i++) {
            if (nums.get(i - 1) < i && nums.get(i) > i) {
                ans++;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<Integer> nums = jsonArrayToIntList(inputJsonValues[0]);
        return JSON.toJSON(countWays(nums));
    }
}
