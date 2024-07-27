package problems.problems_699;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> fallingSquares(int[][] positions) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] positions = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(fallingSquares(positions));
    }
}
