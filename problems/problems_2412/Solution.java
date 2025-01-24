package problems.problems_2412;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long minimumMoney(int[][] transactions) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] transactions = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(minimumMoney(transactions));
    }
}
