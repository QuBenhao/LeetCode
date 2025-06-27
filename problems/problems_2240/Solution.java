package problems.problems_2240;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long waysToBuyPensPencils(int total, int cost1, int cost2) {
        long ans = 0;
        while (total >= 0) {
            ans += total / cost2 + 1;
            total -= cost1;
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int total = Integer.parseInt(inputJsonValues[0]);
		int cost1 = Integer.parseInt(inputJsonValues[1]);
		int cost2 = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(waysToBuyPensPencils(total, cost1, cost2));
    }
}
