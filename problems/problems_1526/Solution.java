package problems.problems_1526;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minNumberOperations(int[] target) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] target = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(minNumberOperations(target));
    }
}
