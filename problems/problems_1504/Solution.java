package problems.problems_1504;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numSubmat(int[][] mat) {
        int n = mat[0].length;
        int ans = 0;
        int[] heights = new int[n];
        for (int[] row: mat) {
            List<Integer> st = new ArrayList<>();
            int[] prev = new int[n];
            int preSum = 0;
            for (int j = 0; j < n; ++j) {
                heights[j] = row[j] == 0 ? 0 : heights[j] + 1;
                while (!st.isEmpty() && heights[st.getLast()] >= heights[j]) {
                    preSum -= prev[st.removeLast()];
                }
                prev[j] = heights[j] * (st.isEmpty() ? j + 1 : j - st.getLast());
                preSum += prev[j];
                st.add(j);
                ans += preSum;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] mat = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(numSubmat(mat));
    }
}
