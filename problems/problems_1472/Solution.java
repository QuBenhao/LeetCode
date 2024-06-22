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
        
        return JSON.toJSON();
    }
}
