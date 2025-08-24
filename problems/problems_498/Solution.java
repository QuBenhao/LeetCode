package problems.problems_498;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] findDiagonalOrder(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        int[] ans = new int[m * n];
        for(int k = 0, idx = 0; k < m + n - 1; k++) {
            if ((k & 1) == 1) {
                for(int x = Math.max(0, k - n + 1); x < Math.min(k + 1, m); x++) {
                    ans[idx++] = mat[x][k - x];
                }
            } else {
                for (int x = Math.min(k, m - 1); x >= Math.max(0, k - n + 1); x--) {
                    ans[idx++] = mat[x][k - x];
                }
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] mat = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(findDiagonalOrder(mat));
    }
}
