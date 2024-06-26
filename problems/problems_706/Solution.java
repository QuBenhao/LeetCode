package problems.problems_706;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class MyHashMap {
	private final Map<Integer, Integer> map;

    public MyHashMap() {
		map = new HashMap<>();
    }
    
    public void put(int key, int value) {
		map.put(key, value);
    }
    
    public int get(int key) {
		return map.getOrDefault(key, -1);
    }
    
    public void remove(int key) {
		map.remove(key);
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] values) {
        String[] operators = jsonArrayToStringArray(values[0]);
		String[][] opValues = jsonArrayToString2DArray(values[1]);
		
		MyHashMap obj = new MyHashMap();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("put") == 0) {
				int key = Integer.parseInt(opValues[i][0]);
				int value = Integer.parseInt(opValues[i][1]);
				obj.put(key, value);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("get") == 0) {
				int key = Integer.parseInt(opValues[i][0]);
				ans.add(obj.get(key));
				continue;
			}
			if (operators[i].compareTo("remove") == 0) {
				int key = Integer.parseInt(opValues[i][0]);
				obj.remove(key);
				ans.add(null);
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
