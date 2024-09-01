package problems.problems_LCR_037;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();
        out:
        for (int asteroid : asteroids) {
            while (!stack.empty() && stack.peek() > 0 && asteroid < 0) {
                int top = stack.pop();
                if (top == -asteroid) {
                    continue out;
                } else if (top > -asteroid) {
                    stack.push(top);
                    continue out;
                }
            }
            stack.push(asteroid);
        }
        int[] res = new int[stack.size()];
        for (int i = res.length - 1; i >= 0; i--) {
            res[i] = stack.pop();
        }
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] asteroids = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(asteroidCollision(asteroids));
    }
}
