package problems.problems_295;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class MedianFinder {

    public MedianFinder() {

    }
    
    public void addNum(int num) {

    }
    
    public double findMedian() {

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
