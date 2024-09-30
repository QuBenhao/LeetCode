package problems.problems_1845;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

import com.alibaba.fastjson.JSON;

import qubhjava.BaseSolution;


class SeatManager {
	private PriorityQueue<Integer> pq;

    public SeatManager(int n) {
		pq = new PriorityQueue<>(n);
		for (int i = 1; i <= n; i++) {
			pq.add(i);
		}
    }
    
    public int reserve() {
		return pq.poll();
    }
    
    public void unreserve(int seatNumber) {
		pq.add(seatNumber);
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = new SeatManager(n);
 * int param_1 = obj.reserve();
 * obj.unreserve(seatNumber);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int n = Integer.parseInt(opValues[0][0]);
		SeatManager obj = new SeatManager(n);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("reserve") == 0) {
				
				ans.add(obj.reserve());
				continue;
			}
			if (operators[i].compareTo("unreserve") == 0) {
				int seatNumber = Integer.parseInt(opValues[i][0]);
				obj.unreserve(seatNumber);
				ans.add(null);
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
