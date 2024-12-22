package problems.problems_855;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class ExamRoom {

    public ExamRoom(int n) {
        
    }
    
    public int seat() {
        
    }
    
    public void leave(int p) {
        
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(n);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int n = Integer.parseInt(opValues[0][0]);
		ExamRoom obj = new ExamRoom(n);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("seat") == 0) {
				
				ans.add(obj.seat());
				continue;
			}
			if (operators[i].compareTo("leave") == 0) {
				int p = Integer.parseInt(opValues[i][0]);
				obj.leave(p);
				ans.add(null);
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
