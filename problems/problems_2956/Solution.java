package problems.problems_2956;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] findIntersectionValues(int[] nums1, int[] nums2) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] nums2 = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(findIntersectionValues(nums1, nums2));
    }
}
