package problems.problems_699;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> fallingSquares(int[][] positions) {
        Set<Integer> points = new HashSet<>();
        for (int[] pos : positions) {
            points.add(pos[0]);
            points.add(pos[0] + pos[1] - 1);
        }
        List<Integer> sortedPoints = new ArrayList<>(points);
        Collections.sort(sortedPoints);
        Map<Integer, Integer> index = new HashMap<>();
        for (int i = 0; i < sortedPoints.size(); i++) {
            index.put(sortedPoints.get(i), i);
        }
        List<Integer> res = new ArrayList<>(positions.length);
        int[] heights = new int[sortedPoints.size()];
        for (int[] pos : positions) {
            int left = index.get(pos[0]), right = index.get(pos[0] + pos[1] - 1);
            int h = 0;
            for (int i = left; i <= right; i++) {
                h = Math.max(h, heights[i]);
            }
            h += pos[1];
            for (int i = left; i <= right; i++) {
                heights[i] = h;
            }
            res.add(res.isEmpty() ? h : Math.max(res.getLast(), h));
        }
        return res;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] positions = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(fallingSquares(positions));
    }
}
