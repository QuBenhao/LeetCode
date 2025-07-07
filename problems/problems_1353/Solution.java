package problems.problems_1353;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int find(int[] fa, int x) {
        if (fa[x] != x) {
            fa[x] = find(fa, fa[x]);
        }
        return fa[x];
    }

    public int maxEvents(int[][] events) {
        Arrays.sort(events, Comparator.comparingInt(o -> o[1]));
        int maxDay = events[events.length - 1][1];
        int[] fa = new int[maxDay + 2];
        for (int i = 0; i < fa.length; ++i) {
            fa[i] = i;
        }
        int ans = 0;
        for (int[] event: events) {
            int x = find(fa, event[0]);
            if (x <= event[1]) {
                ++ans;
                fa[x] = x + 1;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] events = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(maxEvents(events));
    }
}
