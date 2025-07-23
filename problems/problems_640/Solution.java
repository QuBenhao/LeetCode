package problems.problems_640;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String solveEquation(String equation) {
        int k = 0, b = 0, sign = 1, cur = 0;
        char last = '+';
        for (char c: equation.toCharArray()) {
            if ('0' <= c && c <= '9') {
                cur = cur * 10 + c - '0';
            } else {
                if (c == 'x') {
                    if (last != '0' && cur == 0) {
                        cur = 1;
                    }
                    k += sign * cur;
                } else {
                    b += sign * cur;
                    if (c == '=') {
                        sign = 1;
                        k *= -1;
                        b *= -1;
                    } else if (c == '-') {
                        sign = -1;
                    } else if (c == '+') {
                        sign = 1;
                    }
                }
                cur = 0;
            }
            last = c;
        }
        b += sign * cur;
        if (k == 0) {
            return b == 0 ? "Infinite solutions" : "No solution";
        }
        return "x=" + (-b / k);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String equation = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(solveEquation(equation));
    }
}
