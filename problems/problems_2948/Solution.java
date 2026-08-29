package problems.problems_2948;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int limit = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(lexicographicallySmallestArray(nums, limit));
    }
}
