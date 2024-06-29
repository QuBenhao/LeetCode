package problems.problems_78;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<Integer>> subsets(int[] nums) {

    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(subsets(nums));
    }
}
