package problems.problems_2302;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long countSubarrays(int[] nums, long k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		long k = Long.parseLong(inputJsonValues[1]);
        return JSON.toJSON(countSubarrays(nums, k));
    }
}
