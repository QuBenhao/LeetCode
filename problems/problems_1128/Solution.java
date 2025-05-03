package problems.problems_1128;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numEquivDominoPairs(int[][] dominoes) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] dominoes = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(numEquivDominoPairs(dominoes));
    }
}
