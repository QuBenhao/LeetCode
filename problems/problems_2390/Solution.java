package problems.problems_2390;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String removeStars(String s) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '*') {
                if (!sb.isEmpty()) {
                    sb.deleteCharAt(sb.length() - 1);
                }
            } else {
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(removeStars(s));
    }
}
