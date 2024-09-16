package problems.problems_1184;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int distanceBetweenBusStops(int[] distance, int start, int destination) {
        int n = distance.length, min = Math.min(start, destination), max = Math.max(start, destination);
        int clockwise = 0, counterclockwise = 0;
        for (int i = min; i < max; i++) {
            clockwise += distance[i];
        }
        for (int i = max; i < n + min; i++) {
            counterclockwise += distance[i % n];
        }
        return Math.min(clockwise, counterclockwise);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] distance = jsonArrayToIntArray(inputJsonValues[0]);
		int start = Integer.parseInt(inputJsonValues[1]);
		int destination = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(distanceBetweenBusStops(distance, start, destination));
    }
}
