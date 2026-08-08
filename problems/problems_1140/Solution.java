package problems.problems_1140;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int stoneGameII(int[] piles) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] piles = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(stoneGameII(piles));
    }
}
