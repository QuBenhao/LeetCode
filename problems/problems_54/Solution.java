package problems.problems_54;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> spiralOrder(int[][] matrix) {

    }

    @Override
    public Object solve(String[] values) {
        int[][] matrix = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(spiralOrder(matrix));
    }
}
