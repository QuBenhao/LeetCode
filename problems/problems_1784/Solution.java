package problems.problems_1784;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean checkOnesSegment(String s) {
        int count = 0;
        boolean appear = false;
        for (char c: s.toCharArray()) {
            if (c == '1') {
                appear = true;
            } else {
                if (appear) {
                    if (++count > 1) {
                        return false;
                    }
                    appear = false;
                }
            }
        }
        return count == 0 || !appear;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(checkOnesSegment(s));
    }
}
