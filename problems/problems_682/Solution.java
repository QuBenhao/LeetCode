package problems.problems_682;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int calPoints(String[] operations) {
        int ans = 0;
        Stack<Integer> stack = new Stack<>();
        for (String op: operations) {
            switch (op) {
                case "D":
                    ans += stack.peek() * 2;
                    stack.add(stack.peek() * 2);
                    break;
                case "+":
                    int last = stack.pop();
                    int cur = stack.peek() + last;
                    ans += cur;
                    stack.add(last);
                    stack.add(cur);
                    break;
                case "C":
                    ans -= stack.pop();
                    break;
                default:
                    stack.add(Integer.parseInt(op));
                    ans += stack.peek();
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        String[] operations = jsonArrayToStringArray(values[0]);
        return JSON.toJSON(calPoints(operations));
    }
}
