package problems.problems_LCR_058;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class MyCalendar {

    public MyCalendar() {

    }
    
    public boolean book(int start, int end) {

    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		MyCalendar obj = new MyCalendar();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("book") == 0) {
				int start = Integer.parseInt(opValues[i][0]);
				int end = Integer.parseInt(opValues[i][1]);
				ans.add(obj.book(start, end));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
