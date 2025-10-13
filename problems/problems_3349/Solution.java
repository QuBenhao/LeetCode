package problems.problems_3349;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean hasIncreasingSubarrays(List<Integer> nums, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<Integer> nums = jsonArrayToIntList(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(hasIncreasingSubarrays(nums, k));
    }
}
