package problems.problems_1323;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximum69Number (int num) {
        String s = String.valueOf(num);
        char[] chars = s.toCharArray();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == '6') {
                chars[i] = '9';
                break;
            }
        }
        return Integer.parseInt(new String(chars));
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int num = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON((num));
    }
}
