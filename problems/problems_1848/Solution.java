package problems.problems_1848;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int getMinDistance(int[] nums, int target, int start) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
		int target = Integer.parseInt(inputJsonValues[1]);
		int start = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(getMinDistance(nums, target, start));
    }
}
