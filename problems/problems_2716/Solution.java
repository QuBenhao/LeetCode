package problems.problems_2716;

import java.util.HashSet;
import java.util.Set;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimizedStringLength(String s) {
        Set<Character> st = new HashSet<>();
        int ans = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (st.contains(c)) {
                continue;
            }
            ans++;
            st.add(c);
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(minimizedStringLength(s));
    }
}
