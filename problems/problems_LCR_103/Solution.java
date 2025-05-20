package problems.problems_LCR_103;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int coinChange(int[] coins, int amount) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] coins = jsonArrayToIntArray(inputJsonValues[0]);
		int amount = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(coinChange(coins, amount));
    }
}
