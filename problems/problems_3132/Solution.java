package problems.problems_3132;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumAddedInteger(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        out:
        for (int i = 2; i >= 0; i--) {
            int quota = 2 - i, diff = nums2[0] - nums1[i], idx = i + 1;
            for (int j = 1; j < nums2.length; j++) {
                while (nums2[j] - nums1[idx] != diff) {
                    if (quota-- == 0) {
                        continue out;
                    }
                    idx++;
                }
                idx++;
            }
            return diff;
        }
        return nums2[0] - nums1[0];
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] nums2 = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minimumAddedInteger(nums1, nums2));
    }
}
