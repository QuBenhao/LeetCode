package problems.problems_1622;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class Fancy {

    public Fancy() {
        
    }
    
    public void append(int val) {
        
    }
    
    public void addAll(int inc) {
        
    }
    
    public void multAll(int m) {
        
    }
    
    public int getIndex(int idx) {
        
    }
}

/**
 * Your Fancy object will be instantiated and called as such:
 * Fancy obj = new Fancy();
 * obj.append(val);
 * obj.addAll(inc);
 * obj.multAll(m);
 * int param_4 = obj.getIndex(idx);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		Fancy obj = new Fancy();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("append") == 0) {
				int val = Integer.parseInt(opValues[i][0]);
				obj.append(val);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("addAll") == 0) {
				int inc = Integer.parseInt(opValues[i][0]);
				obj.addAll(inc);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("multAll") == 0) {
				int m = Integer.parseInt(opValues[i][0]);
				obj.multAll(m);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("getIndex") == 0) {
				int idx = Integer.parseInt(opValues[i][0]);
				ans.add(obj.getIndex(idx));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
