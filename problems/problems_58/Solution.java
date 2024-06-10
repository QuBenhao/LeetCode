package problems.problems_58;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int lengthOfLastWord(String s) {
        int i, idx = s.length() - 1;
        for (; idx >= 0 && s.charAt(idx) == ' '; idx--) {
        }
        for (i = idx - 1; i >= 0 && s.charAt(i) != ' '; i--) {
        }
        return idx - i;
    }

    @Override
    public Object solve(String[] values) {
        String s = values[0];
        return JSON.toJSON(lengthOfLastWord(s));
    }
}
