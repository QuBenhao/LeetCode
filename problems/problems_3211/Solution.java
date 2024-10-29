package problems.problems_3211;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private void dfs(int i, int n, List<String> ans, StringBuilder sb) {
        if (i == n) {
            ans.add(sb.toString());
            return;
        }
        if (i == 0 || sb.charAt(i - 1) == '1') {
            sb.append('0');
            dfs(i + 1, n, ans, sb);
            sb.deleteCharAt(sb.length() - 1);
        }
        sb.append('1');
        dfs(i + 1, n, ans, sb);
        sb.deleteCharAt(sb.length() - 1);
    }

    public List<String> validStrings(int n) {
        List<String> ans = new ArrayList<>();
        dfs(0, n, ans, new StringBuilder());
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(validStrings(n));
    }
}
