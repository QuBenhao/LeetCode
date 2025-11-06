package problems.problems_2528;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long maxPower(int[] stations, int r, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] stations = jsonArrayToIntArray(inputJsonValues[0]);
		int r = Integer.parseInt(inputJsonValues[1]);
		int k = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(maxPower(stations, r, k));
    }
}
