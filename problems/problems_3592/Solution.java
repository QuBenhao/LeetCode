package problems.problems_3592;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> findCoins(int[] numWays) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] numWays = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(findCoins(numWays));
    }
}
