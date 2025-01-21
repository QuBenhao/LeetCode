package problems.problems_1561;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxCoins(int[] piles) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] piles = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxCoins(piles));
    }
}
