package problems.problems_593;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        int[] distances = {
            distance(p1, p2), distance(p1, p3), distance(p1, p4),
            distance(p2, p3), distance(p2, p4), distance(p3, p4)
        };
        Arrays.sort(distances);
        return distances[0] > 0 && distances[0] == distances[1] &&
            distances[0] == distances[2] && distances[0] == distances[3] &&
            distances[4] == distances[5] && distances[4] == 2 * distances[0];
    }

    private int distance(int[] a, int[] b) {
        return (a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1]);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] p1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] p2 = jsonArrayToIntArray(inputJsonValues[1]);
		int[] p3 = jsonArrayToIntArray(inputJsonValues[2]);
		int[] p4 = jsonArrayToIntArray(inputJsonValues[3]);
        return JSON.toJSON(validSquare(p1, p2, p3, p4));
    }
}
