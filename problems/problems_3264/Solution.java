package problems.problems_3264;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int multiplier = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(getFinalState(nums, k, multiplier));
    }
}
