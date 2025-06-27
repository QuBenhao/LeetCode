package problems.problems_228;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private String formatRange(int left, int right) {
        if (left == right) {
            return String.valueOf(left);
        } else {
            return String.format("%d->%d", left, right);
        }
    }
    public List<String> summaryRanges(int[] nums) {
        List<String> result = new ArrayList<>();
        int n = nums.length;
        int left = 0, right = 0;
        for (int i = 0; i <= n; ++i) {
            if (i == 0 || i == n || nums[i] != nums[i - 1] + 1) {
                if (i != 0) {
                    result.add(formatRange(left, right));
                }
                if (i < n) {
                    left = right = nums[i];
                }
            } else {
                ++right;
            }
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(summaryRanges(nums));
    }
}
