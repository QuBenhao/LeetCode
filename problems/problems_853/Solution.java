package problems.problems_853;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int carFleet(int target, int[] position, int[] speed) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int target = Integer.parseInt(inputJsonValues[0]);
		int[] position = jsonArrayToIntArray(inputJsonValues[1]);
		int[] speed = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(carFleet(target, position, speed));
    }
}
