package problems.problems_15;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<Integer>> threeSum(int[] nums) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(threeSum(nums));
    }
}
