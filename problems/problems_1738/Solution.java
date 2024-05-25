package problems.problems_1738;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int kthLargestValue(int[][] matrix, int k) {

    }

    @Override
    public Object solve(String[] values) {
        int[][] matrix = jsonArrayToInt2DArray(values[0]);
		int k = Integer.parseInt(values[1]);
        return JSON.toJSON(kthLargestValue(matrix, k));
    }
}
