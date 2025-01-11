package problems.problems_2275;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int largestCombination(int[] candidates) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] candidates = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(largestCombination(candidates));
    }
}
