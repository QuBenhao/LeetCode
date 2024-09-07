package problems.problems_146;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class LRUCache {

    public LRUCache(int capacity) {

    }
    
    public int get(int key) {

    }
    
    public void put(int key, int value) {

    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int capacity = Integer.parseInt(opValues[0][0]);
		LRUCache obj = new LRUCache(capacity);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("get") == 0) {
				int key = Integer.parseInt(opValues[i][0]);
				ans.add(obj.get(key));
				continue;
			}
			if (operators[i].compareTo("put") == 0) {
				int key = Integer.parseInt(opValues[i][0]);
				int value = Integer.parseInt(opValues[i][1]);
				obj.put(key, value);
				ans.add(null);
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
