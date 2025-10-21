package problems.problems_3347;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxFrequency(int[] nums, int k, int numOperations) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int numOperations = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maxFrequency(nums, k, numOperations));
    }
}
