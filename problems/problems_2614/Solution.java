package problems.problems_2614;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int diagonalPrime(int[][] nums) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] nums = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(diagonalPrime(nums));
    }
}
