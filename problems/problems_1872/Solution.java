package problems.problems_1872;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int stoneGameVIII(int[] stones) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] stones = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(stoneGameVIII(stones));
    }
}
