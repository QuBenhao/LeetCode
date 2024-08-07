package problems.problems_950;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] deckRevealedIncreasing(int[] deck) {
        Deque<Integer> ans = new ArrayDeque<>();
        Arrays.sort(deck);
        for (int i = deck.length - 1; i >= 0; i--) {
            if (!ans.isEmpty()) {
                ans.addFirst(ans.pollLast());
            }
            ans.addFirst(deck[i]);
        }
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] deck = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(deckRevealedIncreasing(deck));
    }
}
