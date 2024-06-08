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
        int res1 = helper(2, n - 1, nums[0] + nums[1]); // 删除前两个数
        int res2 = helper(0, n - 3, nums[n - 2] + nums[n - 1]); // 删除后两个数
        int res3 = helper(1, n - 2, nums[0] + nums[n - 1]); // 删除第一个和最后一个数
        return Math.max(Math.max(res1, res2), res3) + 1; // 加上第一次操作
    }

    private int helper(int i, int j, int target) {
        if (done) { // 说明之前已经算出了 res = n / 2
            return 0; // 返回任意 <= n/2 的数均可
        }
        for (int[] row : memo) {
            Arrays.fill(row, -1); // -1 表示没有计算过
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
        if (memo[i][j] != -1) { // 之前计算过
            return memo[i][j];
        }
        int res = 0;
        if (nums[i] + nums[i + 1] == target) { // 删除前两个数
            res = Math.max(res, dfs(i + 2, j, target) + 1);
        }
        if (nums[j - 1] + nums[j] == target) { // 删除后两个数
            res = Math.max(res, dfs(i, j - 2, target) + 1);
        }
        if (nums[i] + nums[j] == target) { // 删除第一个和最后一个数
            res = Math.max(res, dfs(i + 1, j - 1, target) + 1);
        }
        return memo[i][j] = res; // 记忆化
    }

    @Override
    public Object solve(String[] values) {
        int[] nums = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(maxOperations(nums));
    }
}
