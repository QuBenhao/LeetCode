package problems.problems_155;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class MinStack {
	private Stack<Integer> data, helper;

    public MinStack() {
		data = new Stack<>();
		helper = new Stack<>();
    }
    
    public void push(int val) {
		data.push(val);
		if (helper.empty() || helper.lastElement() >= val) {
			helper.push(val);
		} else {
			helper.push(helper.lastElement());
		}
    }
    
    public void pop() {
		data.pop();
		helper.pop();
    }
    
    public int top() {
		return data.lastElement();
    }
    
    public int getMin() {
		return helper.lastElement();
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
