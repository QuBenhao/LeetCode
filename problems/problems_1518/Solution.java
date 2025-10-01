package problems.problems_1518;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numWaterBottles(int numBottles, int numExchange) {
        return numBottles + (numBottles - 1) / (numExchange - 1);   
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int numBottles = Integer.parseInt(inputJsonValues[0]);
		int numExchange = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(numWaterBottles(numBottles, numExchange));
    }
}
