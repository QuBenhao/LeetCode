package problems.problems_1472;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
class BrowserHistory {
    Stack<String> b, f;

    public BrowserHistory(String homepage) {
        b = new Stack<>();
        b.add(homepage);
        f = new Stack<>();
    }
    
    public void visit(String url) {
        b.add(url);
        f.clear();
    }
    
    public String back(int steps) {
        steps = Math.min(steps, b.size() - 1);
        for (int i = 0; i < steps; i++) {
            f.add(b.pop());
        }
        return b.peek();
    }
    
    public String forward(int steps) {
        steps = Math.min(steps, f.size());
        for (int i = 0; i < steps; i++) {
            b.add(f.pop());
        }
        return b.peek();
    }
}
/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] values) {
        String[] operators = jsonArrayToStringArray(values[0]);
        String[][] opValues = jsonArrayToString2DArray(values[1]);
        BrowserHistory obj = new BrowserHistory(jsonStringToString(opValues[0][0]));
        List<Object> result = new ArrayList<>(operators.length);
        result.add(null);
        for (int i = 1; i < operators.length; i++) {
            if (operators[i].compareTo("visit") == 0) {
                obj.visit(jsonStringToString(opValues[i][0]));
                result.add(null);
                continue;
            }
            if (operators[i].compareTo("back") == 0) {
                result.add(obj.back(Integer.parseInt(opValues[i][0])));
                continue;
            }
            if (operators[i].compareTo("forward") == 0) {
                result.add(obj.forward(Integer.parseInt(opValues[i][0])));
                continue;
            }
            result.add(null);
        }
        return JSON.toJSON(result);
    }
}
