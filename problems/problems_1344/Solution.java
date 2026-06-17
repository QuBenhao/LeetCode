package problems.problems_1344;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double angleClock(int hour, int minutes) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int hour = Integer.parseInt(inputJsonValues[0]);
		int minutes = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(angleClock(hour, minutes));
    }
}
