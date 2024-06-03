package problems.problems_3067;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] countPairsOfConnectableServers(int[][] edges, int signalSpeed) {

    }

    @Override
    public Object solve(String[] values) {
        int[][] edges = jsonArrayToInt2DArray(values[0]);
		int signalSpeed = Integer.parseInt(values[1]);
        return JSON.toJSON(countPairsOfConnectableServers(edges, signalSpeed));
    }
}
