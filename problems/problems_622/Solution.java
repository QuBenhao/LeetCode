package problems.problems_622;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class MyCircularQueue {
	private final int k;
	private final int[] arr;
	private int sz; // current size
	private int idx; // index of the next element to be dequeued

    public MyCircularQueue(int k) {
    	this.k = k;
    	this.arr = new int[k];
    	this.sz = 0;
    	this.idx = 0;
    }
    
    public boolean enQueue(int value) {
    	if (sz == k) {
    		return false;
    	}
    	arr[idx] = value;
    	idx = (idx + 1) % k;
    	++sz;
    	return true;
    }
    
    public boolean deQueue() {
    	if (sz == 0) {
    		return false;
    	}
    	--sz;
    	return true;
    }
    
    public int Front() {
    	if (sz == 0) {
    		return -1;
    	}
    	return arr[(idx - sz + k) % k];
    }
    
    public int Rear() {
    	if (sz == 0) {
    		return -1;
    	}
    	return arr[(idx - 1 + k) % k];
    }

    public boolean isEmpty() {
    	return sz == 0;
    }
    
    public boolean isFull() {
    	return sz == k;
    }
}

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int k = Integer.parseInt(opValues[0][0]);
		MyCircularQueue obj = new MyCircularQueue(k);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("enQueue") == 0) {
				int value = Integer.parseInt(opValues[i][0]);
				ans.add(obj.enQueue(value));
				continue;
			}
			if (operators[i].compareTo("deQueue") == 0) {
				
				ans.add(obj.deQueue());
				continue;
			}
			if (operators[i].compareTo("Front") == 0) {
				
				ans.add(obj.Front());
				continue;
			}
			if (operators[i].compareTo("Rear") == 0) {
				
				ans.add(obj.Rear());
				continue;
			}
			if (operators[i].compareTo("isEmpty") == 0) {
				
				ans.add(obj.isEmpty());
				continue;
			}
			if (operators[i].compareTo("isFull") == 0) {
				
				ans.add(obj.isFull());
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
