package problems.problems_295;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


class MedianFinder {
	PriorityQueue<Integer> left, right;
    public MedianFinder() {
		left = new PriorityQueue<>((a, b) -> b - a);
		right = new PriorityQueue<>((a, b) -> a - b);
    }
    
    public void addNum(int num) {
		if (left.size() == right.size()) {
			if (right.isEmpty() || num <= right.peek()) {
				left.add(num);
			} else {
				left.add(right.poll());
				right.add(num);
			}
		} else {
			if (num >= left.peek()) {
				right.add(num);
			} else {
				right.add(left.poll());
				left.add(num);
			}
		}
    }
    
    public double findMedian() {
		return left.size() == right.size() ? (left.peek() + right.peek()) / 2.0 : left.peek();
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		MedianFinder obj = new MedianFinder();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("addNum") == 0) {
				int num = Integer.parseInt(opValues[i][0]);
				obj.addNum(num);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("findMedian") == 0) {
				
				ans.add(obj.findMedian());
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
