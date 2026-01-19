package problems.problems_3314;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] minBitwiseArray(List<Integer> nums) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<Integer> nums = jsonArrayToIntList(inputJsonValues[0]);
        return JSON.toJSON(minBitwiseArray(nums));
    }
}
