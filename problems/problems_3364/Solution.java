package problems.problems_3364;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumSumSubarray(List<Integer> nums, int l, int r) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<Integer> nums = jsonArrayToIntList(inputJsonValues[0]);
		int l = Integer.parseInt(inputJsonValues[1]);
		int r = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(minimumSumSubarray(nums, l, r));
    }
}
