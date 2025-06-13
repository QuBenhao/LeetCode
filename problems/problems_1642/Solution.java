package problems.problems_1642;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int furthestBuilding(int[] heights, int bricks, int ladders) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        int n = heights.length;
        for (int i = 0; i < n - 1; ++i) {
            int diff = heights[i+1] - heights[i];
            if (diff <= 0) continue;
            if (bricks >= diff) {
                bricks -= diff;
                maxHeap.add(diff);
            } else if (ladders > 0) {
                if (!maxHeap.isEmpty() && maxHeap.peek() > diff) {
                    bricks += maxHeap.poll() - diff;
                    maxHeap.add(diff);
                }
                --ladders;
            } else {
                return i;
            }
        }
        return n-1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] heights = jsonArrayToIntArray(inputJsonValues[0]);
		int bricks = Integer.parseInt(inputJsonValues[1]);
		int ladders = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(furthestBuilding(heights, bricks, ladders));
    }
}
