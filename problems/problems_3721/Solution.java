package problems.problems_3721;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int longestBalanced(int[] nums) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(longestBalanced(nums));
    }
}
