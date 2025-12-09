package problems.problems_3577;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countPermutations(int[] complexity) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] complexity = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(countPermutations(complexity));
    }
}
