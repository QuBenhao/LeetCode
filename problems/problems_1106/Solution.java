package problems.problems_1106;

import com.alibaba.fastjson.JSON;

import java.util.*;

import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean parseBoolExpr(String expression) {
        Stack<List<Boolean>> stack = new Stack<>();
        Stack<Character> operators = new Stack<>();
        stack.push(new ArrayList<>());
        for (char c : expression.toCharArray()) {
            switch (c) {
                case ',':
                    continue;
                case 't':
                    stack.peek().add(true);
                    break;
                case 'f':
                    stack.peek().add(false);
                    break;
                case '(':
                    stack.push(new ArrayList<>());
                    break;
                case ')': {
                    List<Boolean> list = stack.pop();
                    char operator = operators.pop();
                    boolean result = false;
                    switch (operator) {
                        case '!':
                            result = !list.getFirst();
                            break;
                        case '&':
                            result = true;
                            for (boolean b : list) {
                                result &= b;
                                if (!result) break;
                            }
                            break;
                        case '|':
                            result = false;
                            for (boolean b : list) {
                                result |= b;
                                if (result) break;
                            }
                            break;
                    }
                    stack.peek().add(result);
                    break;
                }
                default:
                    operators.push(c);
            }
        }
        return stack.peek().getFirst();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String expression = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(parseBoolExpr(expression));
    }
}
