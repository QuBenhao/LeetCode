package problems.problems_777;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canTransform(String start, String result) {
        int l = 0, r = 0;
        int n = start.length();
        for (int i = 0; i < n; ++i) {
            if ((start.charAt(i) == 'L' && r != 0) || (start.charAt(i) == 'R' && l != 0)) {
                return false;
            }
            l += start.charAt(i) == 'L' ? 1 : 0;
            r += start.charAt(i) == 'R' ? 1 : 0;
            l -= result.charAt(i) == 'L' ? 1 : 0;
            r -= result.charAt(i) == 'R' ? 1 : 0;
            if ((l != 0 && r != 0) || l > 0 || r < 0) {
                return false;
            }
        }
        return l == 0 && r == 0;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String start = jsonStringToString(inputJsonValues[0]);
		String result = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(canTransform(start, result));
    }
}
