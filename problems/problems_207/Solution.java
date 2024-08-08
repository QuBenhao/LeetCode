package problems.problems_207;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] degree = new int[numCourses];
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] req: prerequisites) {
            degree[req[0]]++;
            if (!graph.containsKey(req[1])) {
                graph.put(req[1], new ArrayList<>());
            }
            graph.get(req[1]).add(req[0]);
        }
        Deque<Integer> q = new ArrayDeque<>();
        for (int idx = 0; idx < degree.length; idx++) {
            if (degree[idx] == 0) {
                q.offerLast(idx);
            }
        }
        int explored = 0;
        while (!q.isEmpty()) {
            int cur = q.pollFirst();
            explored++;
            if (graph.containsKey(cur)) {
                for (int other: graph.get(cur)) {
                    degree[other]--;
                    if (degree[other] == 0) {
                        q.offerLast(other);
                    }
                }
            }
        }
        return explored == numCourses;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int numCourses = Integer.parseInt(inputJsonValues[0]);
		int[][] prerequisites = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(canFinish(numCourses, prerequisites));
    }
}
