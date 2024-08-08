package problems.problems_3131;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int addedInteger(int[] nums1, int[] nums2) {
        int m1 = nums1[0], m2 = nums2[0];
        for (int v: nums1) {
            m1 = Math.min(m1, v);
        }
        for (int v: nums2) {
            m2 = Math.min(m2, v);
        }
        return m2 - m1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] nums2 = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(addedInteger(nums1, nums2));
    }
}
