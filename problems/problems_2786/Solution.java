package problems.problems_2786;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maxScore(int[] nums, int x) {

    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
		int x = Integer.parseInt(values[1]);
        return JSON.toJSON(maxScore(nums, x));
    }
}
