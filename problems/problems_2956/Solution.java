package problems.problems_2956;

import com.alibaba.fastjson.JSON;

import java.util.*;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] findIntersectionValues(int[] nums1, int[] nums2) {
        int[] ans = new int[2];
        Map<Integer, Integer> counter = new HashMap<>();
        for (int num : nums1) {
            counter.put(num, counter.getOrDefault(num, 0) + 1);
        }
        for (int num : nums2) {
            if (!counter.containsKey(num)) continue;
            ans[1]++;
            ans[0] += counter.get(num);
            counter.put(num, 0);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums1 = jsonArrayToIntArray(inputJsonValues[0]);
        int[] nums2 = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(findIntersectionValues(nums1, nums2));
    }
}
