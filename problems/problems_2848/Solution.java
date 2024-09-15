package problems.problems_2848;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfPoints(List<List<Integer>> nums) {
        nums.sort(Comparator.comparingInt(List::getFirst));
        int ans = 0, cur = nums.getFirst().getFirst() - 1;
        for (List<Integer> num : nums) {
            int left = num.getFirst(), right = num.getLast();
            if (left > cur) {
                ans += right - left + 1;
                cur = right;
            } else if (right > cur) {
                ans += right - cur;
                cur = right;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<List<Integer>> nums = jsonArrayTo2DIntList(inputJsonValues[0]);
        return JSON.toJSON(numberOfPoints(nums));
    }
}
