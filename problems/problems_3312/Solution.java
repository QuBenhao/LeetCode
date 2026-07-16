package problems.problems_3312;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] gcdValues(int[] nums, long[] queries) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		long[] queries = jsonArrayToLongArray(inputJsonValues[1]);
        return JSON.toJSON(gcdValues(nums, queries));
    }
}
