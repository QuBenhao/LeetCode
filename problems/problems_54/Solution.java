package problems.problems_54;

import com.alibaba.fastjson.JSON;

import java.util.*;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> spiralOrder(int[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) {
            return new ArrayList<>();
        }
        List<Integer> ans = new ArrayList<>();
        for (int left = 0, right = matrix[0].length - 1, top = 0, bottom = matrix.length - 1;
             left <= right && top <= bottom; left++, right--, top++, bottom--) {
            for (int col = left; col <= right; col++) {
                ans.add(matrix[top][col]);
            }
            for (int row = top + 1; row <= bottom; row++) {
                ans.add(matrix[row][right]);
            }
            if (left < right && top < bottom) {
                for (int col = right - 1; col > left; col--) {
                    ans.add(matrix[bottom][col]);
                }
                for (int row = bottom; row > top; row--) {
                    ans.add(matrix[row][left]);
                }
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int[][] matrix = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(spiralOrder(matrix));
    }
}
