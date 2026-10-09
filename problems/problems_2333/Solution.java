package problems.problems_2333;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minSumSquareDiff(int[] nums1, int[] nums2, int k1, int k2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] nums2 = jsonArrayToIntArray(inputJsonValues[1]);
		int k1 = Integer.parseInt(inputJsonValues[2]);
		int k2 = Integer.parseInt(inputJsonValues[3]);
        return JSON.toJSON(minSumSquareDiff(nums1, nums2, k1, k2));
    }
}
