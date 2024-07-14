package problems.problems_155;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class MinStack {

    public MinStack() {

    }
    
    public void push(int val) {

    }
    
    public void pop() {

    }
    
    public int top() {

    }
    
    public int getMin() {

    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		MinStack obj = new MinStack();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("push") == 0) {
				int val = Integer.parseInt(opValues[i][0]);
				obj.push(val);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("pop") == 0) {
				
				obj.pop();
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("top") == 0) {
				
				ans.add(obj.top());
				continue;
			}
			if (operators[i].compareTo("getMin") == 0) {
				
				ans.add(obj.getMin());
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
