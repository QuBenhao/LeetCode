package problems.problems_2598;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findSmallestInteger(int[] nums, int value) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int value = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(findSmallestInteger(nums, value));
    }
}
