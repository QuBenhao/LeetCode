package problems.problems_3629;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final int MAX_N = 1000001;
    private static final List<Integer>[] PRIME_FACTORS = new List[MAX_N];
    static {
        for (int i = 0; i < MAX_N; ++i) {
            PRIME_FACTORS[i] = new ArrayList<>();
        }
        for (int i = 2; i < MAX_N; ++i) {
            if (PRIME_FACTORS[i].isEmpty()) {
                for (int j = i; j < MAX_N; j += i) {
                    PRIME_FACTORS[j].add(i);
                }
            }
        }
    }
    public int minJumps(int[] nums) {
        int n = nums.length;
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            int num = nums[i];
            for (int prime : PRIME_FACTORS[num]) {
                graph.putIfAbsent(prime, new ArrayList<>());
                graph.get(prime).add(i);
            }
        }
        Deque<Integer> queue = new ArrayDeque<>();
        boolean[] visited = new boolean[n];
        queue.offer(0);
        visited[0] = true;
        int steps = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; ++i) {
                int index = queue.pollFirst();
                if (index == n - 1) {
                    return steps;
                }
                if (PRIME_FACTORS[nums[index]].size() == 1 && graph.containsKey(nums[index])) {
                    for (int nxt: graph.get(nums[index])) {
                        if (!visited[nxt]) {
                            visited[nxt] = true;
                            queue.offerLast(nxt);
                        }
                    }
                    graph.remove(nums[index]);
                }
                if (!visited[index+1]) {
                    visited[index + 1] = true;
                    queue.offerLast(index + 1);
                }
                if (index > 0 && !visited[index - 1]) {
                    visited[index - 1] = true;
                    queue.offerLast(index - 1);
                }
            }
            ++steps;
        }
        return -1; // If we cannot reach the last index
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(minJumps(nums));
    }
}
