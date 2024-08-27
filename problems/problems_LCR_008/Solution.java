package problems.problems_LCR_008;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minSubArrayLen(int target, int[] nums) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int target = Integer.parseInt(inputJsonValues[0]);
		int[] nums = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minSubArrayLen(target, nums));
    }
}
