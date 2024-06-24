package problems.problems_2732;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> goodSubsetofBinaryMatrix(int[][] grid) {

    }

    @Override
    public Object solve(String[] values) {
        int[][] grid = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(goodSubsetofBinaryMatrix(grid));
    }
}
