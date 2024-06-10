package problems.problems_43;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String multiply(String num1, String num2) {
        if (num1.compareTo("0") == 0 || num2.compareTo("0") == 0) {
            return "0";
        }
        int[] res = new int[num1.length() + num2.length()];
        for (int i = num1.length() - 1; i >= 0; i--) {
            int n1 = num1.charAt(i) - '0';
            for (int j = num2.length() - 1; j >= 0; j--) {
                int n2 = num2.charAt(j) - '0';
                int cur = res[i + j + 1] + n1 * n2;
                res[i + j + 1] = cur % 10;
                res[i + j] += cur / 10;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = res[0] == 0 ? 1 : 0; i < res.length; i++) {
            sb.append(res[i]);
        }
        return sb.toString();
    }

    @Override
    public Object solve(String[] values) {
        String num1 = values[0];
		String num2 = values[1];
        return JSON.toJSON(multiply(num1, num2));
    }
}
