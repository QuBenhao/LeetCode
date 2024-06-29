package problems.problems_494;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findTargetSumWays(int[] nums, int target) {

    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
		int target = Integer.parseInt(values[1]);
        return JSON.toJSON(findTargetSumWays(nums, target));
    }
}
