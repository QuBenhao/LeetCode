package problems.problems_3013;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minimumCost(int[] nums, int k, int dist) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int dist = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(minimumCost(nums, k, dist));
    }
}
