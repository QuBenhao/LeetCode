package problems.problems_3679;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minArrivalsToDiscard(int[] arrivals, int w, int m) {
        Deque<Integer> dq = new ArrayDeque<>();
        Map<Integer, Integer> counter = new HashMap<>();
        int ans = 0;
        int n = arrivals.length;
        for (int i = 0; i < n; ++i) {
            while (!dq.isEmpty() && dq.peekFirst() < i - w + 1) {
                int v = counter.get(arrivals[dq.peekFirst()]) - 1;
                counter.put(arrivals[dq.pollFirst()], v);
            }
            if (counter.getOrDefault(arrivals[i], 0) == m) {
                ++ans;
            } else {
                counter.put(arrivals[i], counter.getOrDefault(arrivals[i], 0) + 1);
                dq.addLast(i);
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arrivals = jsonArrayToIntArray(inputJsonValues[0]);
		int w = Integer.parseInt(inputJsonValues[1]);
		int m = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(minArrivalsToDiscard(arrivals, w, m));
    }
}
