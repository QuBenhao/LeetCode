package problems.problems_2844;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumOperations(String num) {
        int n = num.length();
        boolean zero = false, five = false;
        for (int i = n - 1; i >= 0; i--) {
            char c = num.charAt(i);
            if (zero && (c == '0' || c == '5') || five && (c == '2' || c == '7')) {
                return n - i - 2;
            }
            if (c == '0') {
                zero = true;
            }
            if (c == '5') {
                five = true;
            }
        }
        return zero ? n - 1: n;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String num = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(minimumOperations(num));
    }
}
