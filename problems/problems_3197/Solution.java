package problems.problems_3197;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumSum(int[][] grid) {
        return Math.min(solve_(grid), solve_(rotate(grid)));
    }

    private int solve_(int[][] a) {
        int m = a.length;
        int n = a[0].length;
        
        // Precompute the columns of the leftmost and rightmost ones in each row to calculate the minimum rectangle area for the middle region
        int[][] lr = new int[m][2];
        for (int i = 0; i < m; i++) {
            int l = -1;
            int r = 0;
            for (int j = 0; j < n; j++) {
                if (a[i][j] > 0) {
                    if (l < 0) {
                        l = j;
                    }
                    r = j;
                }
            }
            lr[i][0] = l;
            lr[i][1] = r;
        }

        // lt[i+1][j+1] = minimum rectangle area covering all ones in the subrectangle with top-left corner (0,0) and bottom-right corner (i,j)
        int[][] lt = minimumArea(a);
        a = rotate(a);
        // lb[i][j+1] = minimum rectangle area covering all ones in the subrectangle with bottom-left corner (m-1,0) and top-right corner (i,j)
        int[][] lb = rotate(rotate(rotate(minimumArea(a))));
        a = rotate(a);
        // rb[i][j] = minimum rectangle area covering all ones in the subrectangle with bottom-right corner (m-1,n-1) and top-left corner (i,j)
        int[][] rb = rotate(rotate(minimumArea(a)));
        a = rotate(a);
        // rt[i+1][j] = minimum rectangle area covering all ones in the subrectangle with top-right corner (0,n-1) and bottom-left corner (i,j)
        int[][] rt = rotate(minimumArea(a));

        int ans = Integer.MAX_VALUE;
        if (m >= 3) {
            for (int i = 1; i < m; i++) {
                int left = n;
                int right = 0;
                int top = m;
                int bottom = 0;
                for (int j = i + 1; j < m; j++) {
                    int l = lr[j - 1][0];
                    if (l >= 0) {
                        left = Math.min(left, l);
                        right = Math.max(right, lr[j - 1][1]);
                        top = Math.min(top, j - 1);
                        bottom = j - 1;
                    }
                    // Top-left case in the diagram
                    ans = Math.min(ans, lt[i][n] + (right - left + 1) * (bottom - top + 1) + lb[j][n]);
                }
            }
        }

        if (m >= 2 && n >= 2) {
            for (int i = 1; i < m; i++) {
                for (int j = 1; j < n; j++) {
                    // Top-middle case in the diagram
                    ans = Math.min(ans, lt[i][n] + lb[i][j] + rb[i][j]);
                    // Top-right case in the diagram
                    ans = Math.min(ans, lt[i][j] + rt[i][j] + lb[i][n]);
                }
            }
        }
        return ans;
    }

    private int[][] minimumArea(int[][] a) {
        int m = a.length;
        int n = a[0].length;
        // f[i+1][j+1] is the minimum rectangle area covering all ones in the subrectangle with top-left corner (0,0) and bottom-right corner (i,j)
        int[][] f = new int[m + 1][n + 1];
        int[][] border = new int[n][3];
        for (int j = 0; j < n; j++) {
            border[j][0] = -1;
        }
        for (int i = 0; i < m; i++) {
            int left = -1;
            int right = 0;
            for (int j = 0; j < n; j++) {
                if (a[i][j] == 1) {
                    if (left < 0) {
                        left = j;
                    }
                    right = j;
                }
                int[] preB = border[j];
                if (left < 0) { // This row contains only zeros so far
                    f[i + 1][j + 1] = f[i][j + 1]; // Same as the result above
                } else if (preB[0] < 0) { // This row contains a 1; everything above is 0
                    f[i + 1][j + 1] = right - left + 1;
                    border[j][0] = i;
                    border[j][1] = left;
                    border[j][2] = right;
                } else { // Both this row and the area above contain a 1
                    int l = Math.min(preB[1], left);
                    int r = Math.max(preB[2], right);
                    f[i + 1][j + 1] = (r - l + 1) * (i - preB[0] + 1);
                    border[j][1] = l;
                    border[j][2] = r;
                }
            }
        }
        return f;
    }

    private int[][] rotate(int[][] a) {
        int m = a.length;
        int n = a[0].length;
        int[][] b = new int[n][m];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                b[j][m - 1 - i] = a[i][j];
            }
        }
        return b;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] grid = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(minimumSum(grid));
    }
}
