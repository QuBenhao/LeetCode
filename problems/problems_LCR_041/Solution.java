package problems.problems_LCR_041;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class MovingAverage {

    /** Initialize your data structure here. */
    public MovingAverage(int size) {

    }
    
    public double next(int val) {

    }
}

/**
 * Your MovingAverage object will be instantiated and called as such:
 * MovingAverage obj = new MovingAverage(size);
 * double param_1 = obj.next(val);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int size = Integer.parseInt(opValues[0][0]);
		MovingAverage obj = new MovingAverage(size);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("next") == 0) {
				int val = Integer.parseInt(opValues[i][0]);
				ans.add(obj.next(val));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
