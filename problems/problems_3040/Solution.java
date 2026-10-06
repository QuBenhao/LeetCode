package problems.problems_3040;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int[] nums;
    private int[][] memo;
    private boolean done;

    public int maxOperations(int[] nums) {
        this.nums = nums;
        int n = nums.length;
        memo = new int[n][n];
        int res1 = helper(2, n - 1, nums[0] + nums[1]); // Remove the first two numbers
        int res2 = helper(0, n - 3, nums[n - 2] + nums[n - 1]); // Remove the last two numbers
        int res3 = helper(1, n - 2, nums[0] + nums[n - 1]); // Remove the first and last numbers
        return Math.max(Math.max(res1, res2), res3) + 1; // Include the first operation
    }

    private int helper(int i, int j, int target) {
        if (done) { // res = n / 2 has already been found
            return 0; // Any value <= n/2 may be returned
        }
        for (int[] row : memo) {
            Arrays.fill(row, -1); // -1 means not yet computed
        }
        return dfs(i, j, target);
    }

    private int dfs(int i, int j, int target) {
        if (done) {
            return 0;
        }
        if (i >= j) {
            done = true;
            return 0;
        }
        if (memo[i][j] != -1) { // Already computed
            return memo[i][j];
        }
        int res = 0;
        if (nums[i] + nums[i + 1] == target) { // Remove the first two numbers
            res = Math.max(res, dfs(i + 2, j, target) + 1);
        }
        if (nums[j - 1] + nums[j] == target) { // Remove the last two numbers
            res = Math.max(res, dfs(i, j - 2, target) + 1);
        }
        if (nums[i] + nums[j] == target) { // Remove the first and last numbers
            res = Math.max(res, dfs(i + 1, j - 1, target) + 1);
        }
        return memo[i][j] = res; // Memoization
    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(maxOperations(nums));
    }
}
