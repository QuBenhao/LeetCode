package problems.problems_1603;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class ParkingSystem {
    private final int[] parks;

    public ParkingSystem(int big, int medium, int small) {
        parks = new int[]{big, medium, small};
    }
    
    public boolean addCar(int carType) {
        if (this.parks[--carType] <= 0) {
            return false;
        }
        this.parks[carType]--;
        return true;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] values) {
        String[] operators = jsonArrayToStringArray(values[0]);
		String[][] opValues = jsonArrayToString2DArray(values[1]);
		int big = Integer.parseInt(opValues[0][0]);
		int medium = Integer.parseInt(opValues[0][1]);
		int small = Integer.parseInt(opValues[0][2]);
		ParkingSystem obj = new ParkingSystem(big, medium, small);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("addCar") == 0) {
				int carType = Integer.parseInt(opValues[i][0]);
				ans.add(obj.addCar(carType));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
