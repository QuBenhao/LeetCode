package problems.problems_1130;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int mctFromLeafValues(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        int result = 0;
        for (int num: arr) {
            while (!stack.isEmpty() && stack.peek() <= num) {
                int mid = stack.pop();
                if (stack.isEmpty() || stack.peek() > num) {
                    result += mid * num;
                } else {
                    result += mid * Math.min(num, stack.peek());
                }
            }
            stack.push(num);
        }
        while (stack.size() > 1) {
            int mid = stack.pop();
            result += mid * stack.peek();
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(mctFromLeafValues(arr));
    }
}
