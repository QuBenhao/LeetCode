package problems.problems_636;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] exclusiveTime(int n, List<String> logs) {
        int[] ans = new int[n];
        Deque<int[]> stack = new ArrayDeque<>();
        int total = 0;
        for (String log: logs) {
            String[] splits = log.split(":");
            int idx = Integer.parseInt(splits[0]), time = Integer.parseInt(splits[2]);
            boolean isStart = "start".compareTo(splits[1]) == 0;
            if (isStart) {
                stack.addLast(new int[]{time, total});
            } else {
                int[] last = stack.removeLast();
                int diff = (time + 1 - last[0]) - (total - last[1]);
                ans[idx] += diff;
                total += diff;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int n = Integer.parseInt(inputJsonValues[0]);
		List<String> logs = jsonArrayToStringList(inputJsonValues[1]);
        return JSON.toJSON(exclusiveTime(n, logs));
    }
}
