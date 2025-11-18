package problems.problems_2154;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findFinalValue(int[] nums, int original) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int original = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(findFinalValue(nums, original));
    }
}
