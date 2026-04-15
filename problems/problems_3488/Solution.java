package problems.problems_3488;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> solveQueries(int[] nums, int[] queries) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int[] queries = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(solveQueries(nums, queries));
    }
}
