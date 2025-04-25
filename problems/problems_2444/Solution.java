package problems.problems_2444;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long countSubarrays(int[] nums, int minK, int maxK) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int minK = Integer.parseInt(inputJsonValues[1]);
		int maxK = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(countSubarrays(nums, minK, maxK));
    }
}
