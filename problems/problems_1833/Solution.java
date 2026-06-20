package problems.problems_1833;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxIceCream(int[] costs, int coins) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] costs = jsonArrayToIntArray(inputJsonValues[0]);
		int coins = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxIceCream(costs, coins));
    }
}
