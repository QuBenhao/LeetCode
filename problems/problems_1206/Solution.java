package problems.problems_1206;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class Skiplist {

    public Skiplist() {
        
    }
    
    public boolean search(int target) {
        
    }
    
    public void add(int num) {
        
    }
    
    public boolean erase(int num) {
        
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist obj = new Skiplist();
 * boolean param_1 = obj.search(target);
 * obj.add(num);
 * boolean param_3 = obj.erase(num);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		Skiplist obj = new Skiplist();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("search") == 0) {
				int target = Integer.parseInt(opValues[i][0]);
				ans.add(obj.search(target));
				continue;
			}
			if (operators[i].compareTo("add") == 0) {
				int num = Integer.parseInt(opValues[i][0]);
				obj.add(num);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("erase") == 0) {
				int num = Integer.parseInt(opValues[i][0]);
				ans.add(obj.erase(num));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
