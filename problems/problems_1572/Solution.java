package problems.problems_1572;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int diagonalSum(int[][] mat) {

    }

    @Override
    public Object solve(String[] values) {
        int[][] mat = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(diagonalSum(mat));
    }
}
