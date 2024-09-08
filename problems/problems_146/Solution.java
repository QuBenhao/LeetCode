package problems.problems_146;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class DLinkedNode {
	int key;
	int value;
	DLinkedNode prev;
	DLinkedNode next;
	public DLinkedNode() {}
	public DLinkedNode(int _key, int _value) {key = _key; value = _value;}
}


class LRUCache {
	private Map<Integer, DLinkedNode> cache;
	private int capacity;
	private DLinkedNode head, tail;

	private void addNode(DLinkedNode node) {
		node.prev = head;
		node.next = head.next;
		head.next.prev = node;
		head.next = node;
	}

	private void removeNode(DLinkedNode node) {
		if (node.prev != null) {
			node.prev.next = node.next;
		}
		if (node.next != null) {
			node.next.prev = node.prev;
		}
	}

    public LRUCache(int capacity) {
		this.capacity = capacity;
		head = new DLinkedNode();
		tail = new DLinkedNode();
		head.next = tail;
		tail.prev = head;
		cache = new HashMap<>(capacity);
    }
    
    public int get(int key) {
		DLinkedNode node = cache.get(key);
		if (node == null) {
			return -1;
		}
		removeNode(node);
		addNode(node);
		return node.value;
    }
    
    public void put(int key, int value) {
		DLinkedNode node = cache.get(key);
		if (node != null) {
			node.value = value;
			removeNode(node);
			addNode(node);
			return;
		}
		if (cache.size() == capacity) {
			DLinkedNode last = tail.prev;
			removeNode(last);
			cache.remove(last.key);
		}
		DLinkedNode newNode = new DLinkedNode(key, value);
		cache.put(key, newNode);
		addNode(newNode);
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
