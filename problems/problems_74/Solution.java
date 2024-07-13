package problems.problems_74;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        int row = 0, col = n - 1;
        while (row < m && col >= 0) {
            if (matrix[row][col] == target) return true;
            if (matrix[row][col] < target) row++;
            else col--;
        }
        return false;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] matrix = jsonArrayToInt2DArray(inputJsonValues[0]);
		int target = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(searchMatrix(matrix, target));
    }
}
