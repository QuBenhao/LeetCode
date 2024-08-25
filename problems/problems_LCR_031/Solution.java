package problems.problems_LCR_031;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class DoubleLinkedList {
	int key;
	int value;
	DoubleLinkedList prev;
	DoubleLinkedList next;

	public DoubleLinkedList() {
		key = -1;
		value = -1;
	}

	public DoubleLinkedList(int key, int value) {
		this.key = key;
		this.value = value;
	}

	public void insert(DoubleLinkedList node) {
		node.prev = this;
		node.next = this.next;
		if (this.next != null) {
			this.next.prev = node;
		}
		this.next = node;
	}

	public void remove() {
		if (this.prev != null) {
			this.prev.next = this.next;
		}
		if (this.next != null) {
			this.next.prev = this.prev;
		}
	}
}


class LRUCache {

	int capacity;
	Map<Integer, DoubleLinkedList> map;
	DoubleLinkedList head, tail;

    public LRUCache(int capacity) {
		this.capacity = capacity;
		this.map = new HashMap<>(capacity);
		this.head = new DoubleLinkedList();
		this.tail = new DoubleLinkedList();
		this.head.next = this.tail;
		this.tail.prev = this.head;
    }
    
    public int get(int key) {
		if (!map.containsKey(key)) {
			return -1;
		}
		DoubleLinkedList node = map.get(key);
		node.remove();
		head.insert(node);
		return node.value;
    }
    
    public void put(int key, int value) {
		DoubleLinkedList node;
		if (map.containsKey(key)) {
			node = map.get(key);
			node.remove();
			node.value = value;
		} else {
			if (map.size() == capacity) {
				map.remove(tail.prev.key);
				tail.prev.remove();
			}
			node = new DoubleLinkedList(key, value);
			map.put(key, node);
		}
		head.insert(node);
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
