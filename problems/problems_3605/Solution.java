package problems.problems_3605;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minStable(int[] nums, int maxC) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int maxC = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minStable(nums, maxC));
    }
}
