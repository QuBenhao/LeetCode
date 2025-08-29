package problems.problems_735;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] asteroidCollision(int[] asteroids) {
        Deque<Integer> q = new ArrayDeque<>();
        for (int asteroid : asteroids) {
            if (asteroid > 0) {
                q.offerLast(asteroid);
            } else {
                while (!q.isEmpty() && q.peekLast() > 0 && q.peekLast() < -asteroid) {
                    q.pollLast();
                }
                if (q.isEmpty() || q.peekLast() < 0) {
                    q.offerLast(asteroid);
                } else if (q.peekLast() == -asteroid) {
                    q.pollLast();
                }
            }
        }
        int[] ans = new int[q.size()];
        for (int i = 0; i < ans.length; i++) {
            ans[i] = q.pollFirst();
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] asteroids = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(asteroidCollision(asteroids));
    }
}
