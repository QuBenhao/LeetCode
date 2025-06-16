package problems.problems_1206;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;

class SkipNode {
	int value;
	SkipNode[] forward;
	public SkipNode(int value, int level) {
		this.value = value;
		this.forward = new SkipNode[level+1];
	}
}


class Skiplist {
	private static final int MAX_LEVEL = 16;
	private static final double P = 0.25;
	private SkipNode head;
	private int level;

    public Skiplist() {
        head = new SkipNode(-1, MAX_LEVEL);
		level = 0;
    }
    
    public boolean search(int target) {
        SkipNode current = head;
		for (int i = level; i >= 0; i--) {
			while (current.forward[i] != null && current.forward[i].value < target) {
				current = current.forward[i];
			}
		}
		current = current.forward[0];
		return current != null && current.value == target;
    }
    
    public void add(int num) {
        SkipNode[] update = new SkipNode[MAX_LEVEL];
		searchWithUpdate(num, update);
		int nl = newLevel();
		if (nl > level) {
			for (int i = level + 1; i <= nl; i++) {
				update[i] = head;
			}
			level = nl;
		}
		SkipNode newNode = new SkipNode(num, nl);
		for (int i = 0; i <= nl; i++) {
			newNode.forward[i] = update[i].forward[i];
			update[i].forward[i] = newNode;
		}
    }
    
    public boolean erase(int num) {
        SkipNode[] update = new SkipNode[MAX_LEVEL];
		SkipNode current = searchWithUpdate(num, update);
		if (current == null || current.value != num) {
			return false; // Not found
		}
		for (int i = 0; i <= level; i++) {
			if (update[i].forward[i] != current) {
				break; // No need to update further levels
			}
			update[i].forward[i] = current.forward[i];
		}
		// Remove levels if necessary
		while (level > 0 && head.forward[level] == null) {
			level--;
		}
		return true; // Successfully erased
    }

	private int newLevel() {
		int newLevel = 0;
		while (Math.random() < P && newLevel < MAX_LEVEL-1) {
			newLevel++;
		}
		return newLevel;
	}
	
	private SkipNode searchWithUpdate(int num, SkipNode[] update) {
		SkipNode current = head;
		for (int i = level; i >= 0; i--) {
			while (current.forward[i] != null && current.forward[i].value < num) {
				current = current.forward[i];
			}
			update[i] = current;
		}
		return current.forward[0];
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
