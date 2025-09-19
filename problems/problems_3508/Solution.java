package problems.problems_3508;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class Router {

    public Router(int memoryLimit) {
        
    }
    
    public boolean addPacket(int source, int destination, int timestamp) {
        
    }
    
    public int[] forwardPacket() {
        
    }
    
    public int getCount(int destination, int startTime, int endTime) {
        
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * Router obj = new Router(memoryLimit);
 * boolean param_1 = obj.addPacket(source,destination,timestamp);
 * int[] param_2 = obj.forwardPacket();
 * int param_3 = obj.getCount(destination,startTime,endTime);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		int memoryLimit = Integer.parseInt(opValues[0][0]);
		Router obj = new Router(memoryLimit);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("addPacket") == 0) {
				int source = Integer.parseInt(opValues[i][0]);
				int destination = Integer.parseInt(opValues[i][1]);
				int timestamp = Integer.parseInt(opValues[i][2]);
				ans.add(obj.addPacket(source, destination, timestamp));
				continue;
			}
			if (operators[i].compareTo("forwardPacket") == 0) {
				
				ans.add(obj.forwardPacket());
				continue;
			}
			if (operators[i].compareTo("getCount") == 0) {
				int destination = Integer.parseInt(opValues[i][0]);
				int startTime = Integer.parseInt(opValues[i][1]);
				int endTime = Integer.parseInt(opValues[i][2]);
				ans.add(obj.getCount(destination, startTime, endTime));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
