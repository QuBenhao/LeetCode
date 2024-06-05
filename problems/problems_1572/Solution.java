package problems.problems_1572;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int diagonalSum(int[][] mat) {
        int ans = 0, n = mat.length;
        for (int i = 0; i < n; i++) {
            ans += mat[i][i] + mat[i][n - 1 - i];
        }
        return n % 2 == 0 ? ans : ans - mat[n/2][n/2];
    }

    @Override
    public Object solve(String[] values) {
        int[][] mat = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(diagonalSum(mat));
    }
}
