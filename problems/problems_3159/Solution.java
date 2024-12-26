package problems.problems_3159;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] occurrencesOfElement(int[] nums, int[] queries, int x) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int[] queries = jsonArrayToIntArray(inputJsonValues[1]);
		int x = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(occurrencesOfElement(nums, queries, x));
    }
}
