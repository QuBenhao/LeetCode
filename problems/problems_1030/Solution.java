package problems.problems_1030;

import java.util.Arrays;
import java.util.Comparator;

public class Solution {
    public int[][] allCellsDistOrder(int R, int C, int r0, int c0) {
        int[][] cells = new int[R * C][2];
        for (int r = 0; r < R; r++) {
            for (int c = 0; c < C; c++)
                cells[r * C + c] = new int[]{r, c};
        }

        Arrays.sort(cells, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return Math.abs(a[0] - r0) + Math.abs(a[1] - c0)
                        - Math.abs(b[0] - r0) - Math.abs(b[1] - c0);
            }
        });

        return cells;
    }
}
