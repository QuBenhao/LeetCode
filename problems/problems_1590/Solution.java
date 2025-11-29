package problems.problems_1590;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minSubarray(int[] nums, int p) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int p = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minSubarray(nums, p));
    }
}
