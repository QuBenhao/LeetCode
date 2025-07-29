package problems.problems_241;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private List<Integer>[][] dp;
    private List<Integer> dfs(String experssion, int l, int r) {
        if (dp[l][r] != null) {
            return dp[l][r];
        }
        dp[l][r] = new ArrayList<>();
        if (r < l) {
            dp[l][r].add(0);
            return dp[l][r];
        }
        try {
            dp[l][r].add(Integer.parseInt(experssion.substring(l, r + 1)));
            return dp[l][r];
        } catch (NumberFormatException _e) {
            for (int i = l; i <= r; ++i) {
                if (Character.isDigit(experssion.charAt(i))) {
                    continue;
                }
                List<Integer> leftVals = dfs(experssion, l, i - 1);
                List<Integer> rightVals = dfs(experssion, i + 1, r);
                for (int leftVal : leftVals) {
                    for (int rightVal : rightVals) {
                        int result = 0;
                        switch (experssion.charAt(i)) {
                            case '+':
                                result = leftVal + rightVal;
                                break;
                            case '-':
                                result = leftVal - rightVal;
                                break;
                            case '*':
                                result = leftVal * rightVal;
                                break;
                        }
                        dp[l][r].add(result);
                    }
                }
            }
        }
        return dp[l][r];
    }
    public List<Integer> diffWaysToCompute(String expression) {
        int n = expression.length();
        dp = new ArrayList[n][n];
        return dfs(expression, 0, n - 1);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String expression = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(diffWaysToCompute(expression));
    }
}
