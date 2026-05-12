package problems.problems_1674;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minMoves(int[] nums, int limit) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int limit = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minMoves(nums, limit));
    }
}
