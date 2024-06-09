package problems.problems_1672;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximumWealth(int[][] accounts) {

    }

    @Override
    public Object solve(String[] values) {
        int[][] accounts = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(maximumWealth(accounts));
    }
}
