package problems.problems_2030;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;

public class Solution extends BaseSolution {
    public String smallestSubsequence(String s, int k, char letter, int repetition) {
        StringBuilder stack = new StringBuilder(k);
        int letterLeft = 0;
        for (char c : s.toCharArray()) {
            if (c == letter) {
                letterLeft++;
            }
        }
        int letterCount = 0;
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            char c = s.charAt(i);
            while (!stack.isEmpty() && stack.charAt(stack.length() - 1) > c && n - i + stack.length() - 1 >= k &&
                    (c == letter
                            || letterCount + letterLeft - (stack.charAt(stack.length() - 1) == letter ? 1 : 0) >= repetition)) {
                if (stack.charAt(stack.length() - 1) == letter) {
                    --letterCount;
                }
                stack.deleteCharAt(stack.length() - 1);
            }

            if (stack.length() < k) {
                if (c == letter) {
                    ++letterCount;
                    stack.append(c);
                } else if (k - stack.length() > repetition - letterCount) {
                    stack.append(c);
                }
            }
            if (c == letter) {
                --letterLeft;
            }
        }
        return stack.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        int k = Integer.parseInt(inputJsonValues[1]);
        char letter = inputJsonValues[2].length() > 1 ? inputJsonValues[2].charAt(1) : inputJsonValues[2].charAt(0);
        int repetition = Integer.parseInt(inputJsonValues[3]);
        return JSON.toJSON(smallestSubsequence(s, k, letter, repetition));
    }
}
