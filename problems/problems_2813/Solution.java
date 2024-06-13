package problems.problems_2813;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long findMaximumElegance(int[][] items, int k) {
        Arrays.sort(items, (a, b) ->  b[0] - a[0]);
        long ans = 0L, totalProfit = 0L;
        Set<Integer> vis = new HashSet<>();
        Stack<Integer> duplicate = new Stack<>();
        for (int i = 0; i < items.length; i++) {
            int profit = items[i][0], category = items[i][1];
            if (i < k) {
                totalProfit += profit;
                if (!vis.contains(category)) {
                    vis.add(category);
                } else {
                    duplicate.addLast(profit);
                }
            } else if (!duplicate.empty() && !vis.contains(category)) {
                totalProfit += profit - duplicate.pop();
                vis.add(category);
            }
            ans = Math.max(ans, totalProfit + (long)vis.size() * vis.size());
        }
        return ans;
    }

    @Override
    public Object solve(String[] values) {
        int[][] items = jsonArrayToInt2DArray(values[0]);
		int k = Integer.parseInt(values[1]);
        return JSON.toJSON(findMaximumElegance(items, k));
    }
}
