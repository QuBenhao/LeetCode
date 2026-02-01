package problems.problems_3829;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class RideSharingSystem {

    public RideSharingSystem() {
        
    }
    
    public void addRider(int riderId) {
        
    }
    
    public void addDriver(int driverId) {
        
    }
    
    public int[] matchDriverWithRider() {
        
    }
    
    public void cancelRider(int riderId) {
        
    }
}

/**
 * Your RideSharingSystem object will be instantiated and called as such:
 * RideSharingSystem obj = new RideSharingSystem();
 * obj.addRider(riderId);
 * obj.addDriver(driverId);
 * int[] param_3 = obj.matchDriverWithRider();
 * obj.cancelRider(riderId);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		RideSharingSystem obj = new RideSharingSystem();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("addRider") == 0) {
				int riderId = Integer.parseInt(opValues[i][0]);
				obj.addRider(riderId);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("addDriver") == 0) {
				int driverId = Integer.parseInt(opValues[i][0]);
				obj.addDriver(driverId);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("matchDriverWithRider") == 0) {
				
				ans.add(obj.matchDriverWithRider());
				continue;
			}
			if (operators[i].compareTo("cancelRider") == 0) {
				int riderId = Integer.parseInt(opValues[i][0]);
				obj.cancelRider(riderId);
				ans.add(null);
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
