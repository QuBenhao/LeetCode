package problems.problems_3100;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxBottlesDrunk(int numBottles, int numExchange) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int numBottles = Integer.parseInt(inputJsonValues[0]);
		int numExchange = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxBottlesDrunk(numBottles, numExchange));
    }
}
