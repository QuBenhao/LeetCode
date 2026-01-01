package problems.problems_961;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int repeatedNTimes(int[] nums) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(repeatedNTimes(nums));
    }
}
