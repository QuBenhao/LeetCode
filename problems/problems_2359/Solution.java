package problems.problems_2359;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int closestMeetingNode(int[] edges, int node1, int node2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] edges = jsonArrayToIntArray(inputJsonValues[0]);
		int node1 = Integer.parseInt(inputJsonValues[1]);
		int node2 = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(closestMeetingNode(edges, node1, node2));
    }
}
