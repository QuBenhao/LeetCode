package problems.problems_LCR_066;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class MapSum {

    /** Initialize your data structure here. */
    public MapSum() {

    }
    
    public void insert(String key, int val) {

    }
    
    public int sum(String prefix) {

    }
}

/**
 * Your MapSum object will be instantiated and called as such:
 * MapSum obj = new MapSum();
 * obj.insert(key,val);
 * int param_2 = obj.sum(prefix);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		MapSum obj = new MapSum();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("insert") == 0) {
				String key = jsonStringToString(opValues[i][0]);
				int val = Integer.parseInt(opValues[i][1]);
				obj.insert(key, val);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("sum") == 0) {
				String prefix = jsonStringToString(opValues[i][0]);
				ans.add(obj.sum(prefix));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
