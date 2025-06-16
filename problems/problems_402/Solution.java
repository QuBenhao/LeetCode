package problems.problems_402;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String removeKdigits(String num, int k) {
        StringBuilder sb = new StringBuilder();
        for (char c: num.toCharArray()) {
            while (k > 0 && sb.length() > 0 && sb.charAt(sb.length() - 1) > c) {
                sb.deleteCharAt(sb.length() - 1);
                k--;
            }
            sb.append(c);
        }
        while (k > 0 && sb.length() > 0) {
            sb.deleteCharAt(sb.length() - 1);
            k--;
        }
        int startIdx = 0;
        while (startIdx < sb.length() && sb.charAt(startIdx) == '0') {
            startIdx++;
        }
        if (startIdx == sb.length()) {
            return "0";
        }
        return sb.substring(startIdx);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String num = jsonStringToString(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(removeKdigits(num, k));
    }
}
