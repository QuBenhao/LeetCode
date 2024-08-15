package problems.problems_3148;

import java.util.Arrays;
import java.util.List;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxScore(List<List<Integer>> grid) {
        int ans = Integer.MIN_VALUE;
        int n = grid.get(0).size();
        int[] colsMin = new int[n];
        Arrays.fill(colsMin, Integer.MAX_VALUE);
        for (List<Integer> row: grid) {
            int preMin = Integer.MAX_VALUE;
            for (int j = 0; j < n; j++) {
                ans = Math.max(ans, row.get(j) - Math.min(preMin, colsMin[j]));
                colsMin[j] = Math.min(colsMin[j], row.get(j));
                preMin = Math.min(preMin, colsMin[j]);
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<List<Integer>> grid = jsonArrayTo2DIntList(inputJsonValues[0]);
        return JSON.toJSON(maxScore(grid));
    }
}
