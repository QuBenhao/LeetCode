package problems.problems_3068;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maximumValueSum(int[] nums, int k, int[][] edges) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int[][] edges = jsonArrayToInt2DArray(inputJsonValues[2]);
        return JSON.toJSON(maximumValueSum(nums, k, edges));
    }
}
