package problems.problems_73;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public void setZeroes(int[][] matrix) {

    }

    @Override
    public Object solve(String[] values) {
        int[][] matrix = jsonArrayToInt2DArray(values[0]);
		setZeroes(matrix);
        return JSON.toJSON(matrix);
    }
}
