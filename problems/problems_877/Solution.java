package problems.problems_877;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean stoneGame(int[] piles) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] piles = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(stoneGame(piles));
    }
}
