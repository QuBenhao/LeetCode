package problems.problems_2713;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxIncreasingCells(int[][] mat) {

    }

    @Override
    public Object solve(String[] values) {
        int[][] mat = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(maxIncreasingCells(mat));
    }
}
