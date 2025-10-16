package problems.problems_2598;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findSmallestInteger(int[] nums, int value) {
        int[] counts = new int[value];
        for (int num: nums) {
            ++counts[(num % value + value) % value];
        }
        int ans = 0, ansM = counts[0];
        for (int i = 0; i < value; ++i) {
            if (counts[i] < ansM) {
                ansM = counts[i];
                ans = i;
            }
        }
        return ansM * value + ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int value = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(findSmallestInteger(nums, value));
    }
}
