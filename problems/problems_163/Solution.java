package problems.problems_163;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<Integer>> findMissingRanges(int[] nums, int lower, int upper) {

    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
		int lower = Integer.parseInt(values[1]);
		int upper = Integer.parseInt(values[2]);
        return JSON.toJSON(findMissingRanges(nums, lower, upper));
    }
}
