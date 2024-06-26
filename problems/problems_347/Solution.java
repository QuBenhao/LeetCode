package problems.problems_347;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] topKFrequent(int[] nums, int k) {

    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
		int k = Integer.parseInt(values[1]);
        return JSON.toJSON(topKFrequent(nums, k));
    }
}
