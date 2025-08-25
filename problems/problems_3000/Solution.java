package problems.problems_3000;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        int maxLength = 0, maxArea = 0;
        for (int[] dim: dimensions) {
            int a = dim[0], b = dim[1];
            int length = a * a + b * b;
            if (length > maxLength) {
                maxLength = length;
                maxArea = a * b;
            } else if (length == maxLength) {
                maxArea = Math.max(maxArea, a * b);
            }
        }
        return maxArea;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] dimensions = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(areaOfMaxDiagonal(dimensions));
    }
}
