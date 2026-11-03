package problems.problems_3505;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minOperations(int[] nums, int x, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int x = Integer.parseInt(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(minOperations(nums, x, k));
    }
}
