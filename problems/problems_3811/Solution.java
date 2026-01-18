package problems.problems_3811;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int alternatingXOR(int[] nums, int target1, int target2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int target1 = Integer.parseInt(inputJsonValues[1]);
		int target2 = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(alternatingXOR(nums, target1, target2));
    }
}
