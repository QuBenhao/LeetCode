package problems.problems_3806;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumAND(int[] nums, int k, int m) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int m = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maximumAND(nums, k, m));
    }
}
