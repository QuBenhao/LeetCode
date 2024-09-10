package problems.problems_LCR_002;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String addBinary(String a, String b) {
        StringBuilder sb = new StringBuilder();
        if (a.length() < b.length()) {
            String temp = a;
            a = b;
            b = temp;
        }
        int carry = 0;
        for (int i = a.length() - 1, d = a.length() - b.length(); i >= 0; i--) {
            int sum = a.charAt(i) - '0' + (i - d >= 0 ? b.charAt(i - d) - '0' : 0) + carry;
            sb.append(sum % 2);
            carry = sum / 2;
        }
        if (carry != 0) {
            sb.append(carry);
        }
        return sb.reverse().toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String a = jsonStringToString(inputJsonValues[0]);
		String b = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(addBinary(a, b));
    }
}
