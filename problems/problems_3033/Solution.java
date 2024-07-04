package problems.problems_3033;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[][] modifiedMatrix(int[][] matrix) {
        for (int m = matrix.length, n = matrix[0].length, j = 0; j < n; j++) {
            int mx = -1;
            List<Integer> remain = new ArrayList<>();
            for (int i = 0; i < m; i++) {
                if (matrix[i][j] != -1) {
                    mx = Math.max(mx, matrix[i][j]);
                } else {
                    remain.add(i);
                }
            }
            for (int i: remain) {
                matrix[i][j] = mx;
            }
        }
        return matrix;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] matrix = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(modifiedMatrix(matrix));
    }
}
