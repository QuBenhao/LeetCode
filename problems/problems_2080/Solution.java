package problems.problems_2080;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class RangeFreqQuery {

    public RangeFreqQuery(int[] arr) {
        
    }
    
    public int query(int left, int right, int value) {
        
    }
}

/**
 * Your RangeFreqQuery object will be instantiated and called as such:
 * RangeFreqQuery obj = new RangeFreqQuery(arr);
 * int param_1 = obj.query(left,right,value);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int[] arr = jsonArrayToIntArray(opValues[0][0]);
		RangeFreqQuery obj = new RangeFreqQuery(arr);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("query") == 0) {
				int left = Integer.parseInt(opValues[i][0]);
				int right = Integer.parseInt(opValues[i][1]);
				int value = Integer.parseInt(opValues[i][2]);
				ans.add(obj.query(left, right, value));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
