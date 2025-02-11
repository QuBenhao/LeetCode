package problems.problems_1760;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumSize(int[] nums, int maxOperations) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int maxOperations = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minimumSize(nums, maxOperations));
    }
}
