package problems.problems_768;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxChunksToSorted(int[] arr) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (int num: arr) {
            if (!stack.isEmpty() && stack.peekLast() > num) {
                int max = stack.pollLast();
                while (!stack.isEmpty() && stack.peekLast() > num) {
                    max = Math.max(max, stack.pollLast());
                }
                stack.addLast(max);
            } else {
                stack.addLast(num);
            }
        }
        return stack.size();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxChunksToSorted(arr));
    }
}
