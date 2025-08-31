package problems.problems_1792;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public double maxAverageRatio(int[][] classes, int extraStudents) {
        PriorityQueue<double[]> pq = new PriorityQueue<>((a, b) -> Double.compare(b[0], a[0]));
        for (int[] c : classes) {
            int pass = c[0], total = c[1];
            double imp = (double) (pass + 1) / (total + 1) - (double) pass / total;
            pq.offer(new double[]{imp, pass, total});
        }
        while (extraStudents-- > 0) {
            double[] curr = pq.poll();
            curr[1]++;
            curr[2]++;
            double imp =(curr[1] + 1) / (curr[2] + 1) - curr[1] / curr[2];
            pq.offer(new double[]{imp, curr[1], curr[2]});
        }
        double result = 0.0;
        while (!pq.isEmpty()) {
            double[] curr = pq.poll();
            result += curr[1] / curr[2];
        }
        return result / classes.length;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] classes = jsonArrayToInt2DArray(inputJsonValues[0]);
		int extraStudents = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxAverageRatio(classes, extraStudents));
    }
}
