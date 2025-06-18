package problems.problems_791;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String customSortString(String order, String s) {
        int[] count = new int[26];
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }
        StringBuilder result = new StringBuilder();
        for (char c: order.toCharArray()) {
            while (count[c - 'a']-- > 0) {
                result.append(c);
            }
        }
        for (int i = 0; i < 26; ++i) {
            while (count[i]-- > 0) {
                result.append((char) (i + 'a'));
            }
        }
        return result.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String order = jsonStringToString(inputJsonValues[0]);
		String s = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(customSortString(order, s));
    }
}
