package problems.problems_22;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<>();
        backtrack(ans, n, new StringBuilder(), 0, 0);
        return ans;
    }

    private void backtrack(List<String> ans, int n, StringBuilder sb, int left, int right) {
        if (left == n && right == n) {
            ans.add(sb.toString());
            return;
        }
        if (left < n) {
            sb.append('(');
            backtrack(ans, n, sb, left + 1, right);
            sb.deleteCharAt(sb.length() - 1);
        }
        if (right < left) {
            sb.append(')');
            backtrack(ans, n, sb, left, right + 1);
            sb.deleteCharAt(sb.length() - 1);
        }
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(generateParenthesis(n));
    }
}
