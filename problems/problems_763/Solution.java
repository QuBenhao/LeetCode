package problems.problems_763;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> partitionLabels(String s) {
        int[] last = new int[26];
        int n = s.length();
        for (int i = 0; i < n; i++) {
            last[s.charAt(i) - 'a'] = i;
        }
        List<Integer> ans = new ArrayList<>();
        int start = 0, end = 0;
        for (int i = 0; i < n; i++) {
            end = Math.max(end, last[s.charAt(i) - 'a']);
            if (i == end) {
                ans.add(end - start + 1);
                start = end + 1;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        String s = jsonStringToString(values[0]);
        return JSON.toJSON(partitionLabels(s));
    }
}
