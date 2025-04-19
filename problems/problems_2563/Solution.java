package problems.problems_2563;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long countFairPairs(int[] nums, int lower, int upper) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int lower = Integer.parseInt(inputJsonValues[1]);
		int upper = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(countFairPairs(nums, lower, upper));
    }
}
