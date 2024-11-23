package problems.problems_632;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] smallestRange(List<List<Integer>> nums) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<List<Integer>> nums = jsonArrayTo2DIntList(inputJsonValues[0]);
        return JSON.toJSON(smallestRange(nums));
    }
}
