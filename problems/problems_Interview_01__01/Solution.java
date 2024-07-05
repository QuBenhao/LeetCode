package problems.problems_Interview_01__01;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isUnique(String astr) {
        int mark = 0;
        for (int i = 0; i < astr.length(); i++) {
            int cur = 1 << (astr.charAt(i) - 'a');
            if ((mark & cur) != 0) {
                return false;
            }
            mark |= cur;
        }
        return true;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String astr = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(isUnique(astr));
    }
}
