package problems.problems_LCR_030;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


class RandomizedSet {
	private final List<Integer> list;
	private final Map<Integer, Integer> map;
	private final Random random;

    /** Initialize your data structure here. */
    public RandomizedSet() {
		list = new ArrayList<>();
		map = new HashMap<>();
		random = new Random();
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
		if (map.containsKey(val)) {
			return false;
		}
		list.add(val);
		map.put(val, list.size()-1);
		return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
		if (!map.containsKey(val)) {
			return false;
		}
		int idx = map.get(val);
		int v = list.getLast();
		list.set(idx, v);
		map.put(v, idx);
		list.removeLast();
		map.remove(val);
		return true;
    }
    
    /** Get a random element from the set. */
    public int getRandom() {
		return list.get(random.nextInt(list.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		RandomizedSet obj = new RandomizedSet();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("insert") == 0) {
				int val = Integer.parseInt(opValues[i][0]);
				ans.add(obj.insert(val));
				continue;
			}
			if (operators[i].compareTo("remove") == 0) {
				int val = Integer.parseInt(opValues[i][0]);
				ans.add(obj.remove(val));
				continue;
			}
			if (operators[i].compareTo("getRandom") == 0) {
				
				ans.add(obj.getRandom());
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
