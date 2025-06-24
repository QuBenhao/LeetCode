package problems.problems_2040;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long kthSmallestProduct(int[] nums1, int[] nums2, long k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] nums2 = jsonArrayToIntArray(inputJsonValues[1]);
		long k = Long.parseLong(inputJsonValues[2]);
        return JSON.toJSON(kthSmallestProduct(nums1, nums2, k));
    }
}
