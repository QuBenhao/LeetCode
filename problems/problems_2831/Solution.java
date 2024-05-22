package problems.problems_2831;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int longestEqualSubarray(List<Integer> nums, int k) {

    }

    @Override
    public Object solve(String[] values) {
        List<Integer> nums = FIXME(values[0])
		int k = Integer.parseInt(values[1]);
        return JSON.toJSON(longestEqualSubarray(nums, k));
    }
}
