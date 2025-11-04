package problems.problems_3321;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long[] findXSum(int[] nums, int k, int x) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int x = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(findXSum(nums, k, x));
    }
}
