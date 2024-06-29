package problems.problems_2710;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String removeTrailingZeros(String num) {
        int idx = num.length() - 1;
        for (; idx >= 0 && num.charAt(idx) == '0'; idx--) {
        }
        return num.substring(0, idx + 1);
    }

    @Override
    public Object solve(String[] values) {
        String num = jsonStringToString(values[0]);
        return JSON.toJSON(removeTrailingZeros(num));
    }
}
