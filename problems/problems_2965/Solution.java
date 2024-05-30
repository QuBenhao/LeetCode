package problems.problems_2965;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] findMissingAndRepeatedValues(int[][] grid) {

    }

    @Override
    public Object solve(String[] values) {
        int[][] grid = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(findMissingAndRepeatedValues(grid));
    }
}
