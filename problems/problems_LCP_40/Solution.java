package problems.problems_LCP_40;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int replaceSum(int[] cards, int s, int cnt, int x) {
        for (int i = cards.length - cnt - 1; i >= 0; i--) {
            if (cards[i] % 2 != x % 2) {
                return s - x + cards[i];
            }
        }
        return 0;
    }
    public int maxmiumScore(int[] cards, int cnt) {
        Arrays.sort(cards);
        int s = 0, n = cards.length;
        for (int i = n - cnt; i < n; i++) {
            s += cards[i];
        }
        if (s % 2 == 0) {
            return s;
        }
        int cur = cards[n - cnt];
        int ans = replaceSum(cards, s, cnt, cur);
        for (int i = n -cnt + 1; i < n; i++) {
            if (cards[i] % 2 != cur % 2) {
                ans = Math.max(ans, replaceSum(cards, s, cnt, cards[i]));
                break;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] cards = jsonArrayToIntArray(inputJsonValues[0]);
		int cnt = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxmiumScore(cards, cnt));
    }
}
