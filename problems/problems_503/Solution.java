package problems.problems_503;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] nextGreaterElements(int[] nums) {

    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(nextGreaterElements(nums));
    }
}
