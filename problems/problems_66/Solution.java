package problems.problems_66;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] plusOne(int[] digits) {
        for (int i = digits.length - 1, cur = 1; i >= 0; i--) {
            cur += digits[i];
            digits[i] = cur % 10;
            cur /= 10;
            if (cur == 0) {
                return digits;
            }
        }
        int[] arr = new int[digits.length + 1];
        arr[0] = 1;
        return arr;
    }

    @Override
    public Object solve(String[] values) {
        int[] digits = jsonArrayToIntArray(values[0]);
        return JSON.toJSON(plusOne(digits));
    }
}
