package problems.problems_1738;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int kthLargestValue(int[][] matrix, int k) {
        int m = matrix.length;
        int n = matrix[0].length;
        int[] a = new int[m * n];
        int[] colSum = new int[n];
        int i = 0;
        for (int[] row : matrix) {
            int s = 0;
            for (int j = 0; j < row.length; j++) {
                colSum[j] ^= row[j];
                s ^= colSum[j];
                a[i++] = s;
            }
        }
        Arrays.sort(a);
        return a[i - k];
    }


    @Override
    public Object solve(String[] values) {
        int[][] matrix = jsonArrayToInt2DArray(values[0]);
		int k = Integer.parseInt(values[1]);
        return JSON.toJSON(kthLargestValue(matrix, k));
    }
}
