package problems.problems_300;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int lengthOfLIS(int[] nums) {
        List<Integer> stack = new ArrayList<>();
        for (int num : nums) {
            if (stack.isEmpty() || num > stack.getLast()) {
                stack.add(num);
            } else {
                int left = 0, right = stack.size() - 1;
                while (left < right) {
                    int mid = left + (right - left) / 2;
                    if (stack.get(mid) < num) {
                        left = mid + 1;
                    } else {
                        right = mid;
                    }
                }
                stack.set(right, num);
            }
        }
        return stack.size();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(lengthOfLIS(nums));
    }
}
