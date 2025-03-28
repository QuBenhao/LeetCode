package problems.problems_2360;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int longestCycle(int[] edges) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] edges = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(longestCycle(edges));
    }
}
