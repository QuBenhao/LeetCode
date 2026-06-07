package problems.problems_2161;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] pivotArray(int[] nums, int pivot) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int pivot = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(pivotArray(nums, pivot));
    }
}
