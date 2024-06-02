package problems.problems_1523;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countOdds(int low, int high) {

    }

    @Override
    public Object solve(String[] values) {
        int low = Integer.parseInt(values[0]);
		int high = Integer.parseInt(values[1]);
        return JSON.toJSON(countOdds(low, high));
    }
}
