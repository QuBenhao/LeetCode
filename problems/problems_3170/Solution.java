package problems.problems_3170;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String clearStars(String s) {
        int mask = 0;
        int n = s.length();
        char[] chars = s.toCharArray();
        Stack<Integer>[] stacks = new Stack[26];
        Arrays.setAll(stacks, i -> new Stack<Integer>());
        for (int i = 0; i < n; i++) {
            if (chars[i] != '*') {
                int idx = chars[i] - 'a';
                stacks[idx].add(i);
                mask |= 1 << idx;
            } else {
                int idx = Integer.numberOfTrailingZeros(mask);
                Stack<Integer> stack = stacks[idx];
                chars[stack.pop()] = '*';
                if (stack.isEmpty()) {
                    mask &= ~(1 << idx);
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (chars[i] != '*') {
                sb.append(chars[i]);
            }
        }
        return sb.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(clearStars(s));
    }
}
