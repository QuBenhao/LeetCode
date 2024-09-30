package problems.problems_983;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int mincostTickets(int[] days, int[] costs) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] days = jsonArrayToIntArray(inputJsonValues[0]);
		int[] costs = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(mincostTickets(days, costs));
    }
}
