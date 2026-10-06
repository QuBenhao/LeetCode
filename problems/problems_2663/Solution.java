package problems.problems_2663;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String smallestBeautifulString(String S, int k) {
        k += 'a';
        char[] s = S.toCharArray();
        int n = s.length;
        int i = n - 1; // Start with the last letter
        s[i]++; // Increment first
        while (i < n) {
            if (s[i] == k) { // A carry is needed
                if (i == 0) { // Cannot carry
                    return "";
                }
                // Carry
                s[i] = 'a';
                s[--i]++;
            } else if (i > 0 && s[i] == s[i - 1] || i > 1 && s[i] == s[i - 2]) {
                s[i]++; // If s[i] forms a palindrome with characters to its left, keep incrementing s[i]
            } else {
                i++; // Move forward to check for palindromes in the suffix
            }
        }
        return new String(s);
    }



    @Override
    public Object solve(String[] values) {
        String S = jsonStringToString(values[0]);
		int k = Integer.parseInt(values[1]);
        return JSON.toJSON(smallestBeautifulString(S, k));
    }
}
