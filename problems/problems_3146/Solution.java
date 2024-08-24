package problems.problems_3146;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findPermutationDifference(String s, String t) {
        int[] idxes = new int[26];
        for (int i = 0; i < s.length(); i++) {
            idxes[s.charAt(i) - 'a'] += i;
            idxes[t.charAt(i) - 'a'] -= i;
        }
        int ans = 0;
        for (int i: idxes) {
            ans += Math.abs(i);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		String t = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(findPermutationDifference(s, t));
    }
}
