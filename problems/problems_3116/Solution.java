package problems.problems_3116;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long findKthSmallest(int[] coins, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] coins = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(findKthSmallest(coins, k));
    }
}
