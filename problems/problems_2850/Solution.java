package problems.problems_2850;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumMoves(int[][] grid) {
        List<int[]> source = new ArrayList<>(), target = new ArrayList<>();
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid.length; j++) {
                if (grid[i][j] > 1) {
                    for (int k = 0; k < grid[i][j] - 1; k++) {
                        source.add(new int[]{i, j});
                    }
                } else if (grid[i][j] == 0) {
                    target.add(new int[]{i, j});
                }
            }
        }
        int ans = Integer.MAX_VALUE;
        for (List<int[]> sourcePerm : permutations(source)) {
            int total = 0;
            for (int i = 0; i < sourcePerm.size(); i++) {
                total += Math.abs(sourcePerm.get(i)[0] - target.get(i)[0]) + Math.abs(sourcePerm.get(i)[1] - target.get(i)[1]);
            }
            ans = Math.min(ans, total);
        }
        return ans;
    }

    private List<List<int[]>> permutations(List<int[]> arr) {
        List<List<int[]>> result = new ArrayList<>();
        permute(arr, 0, result);
        return result;
    }

    private void permute(List<int[]> arr, int start, List<List<int[]>> result) {
        if (start == arr.size()) {
            result.add(new ArrayList<>(arr));
        }
        for (int i = start; i < arr.size(); i++) {
            swap(arr, start, i);
            permute(arr, start + 1, result);
            swap(arr, start, i);
        }
    }

    private void swap(List<int[]> arr, int i, int j) {
        int[] temp = arr.get(i);
        arr.set(i, arr.get(j));
        arr.set(j, temp);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] grid = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(minimumMoves(grid));
    }
}
