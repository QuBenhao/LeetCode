package problems.problems_3175;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findWinningPlayer(int[] skills, int k) {
        int ans = 0, cur = 0, n = skills.length;
        for (int i = 1; i < n; i++) {
            if (skills[i] < skills[ans]) {
                cur++;
            } else {
                cur = 1;
                ans = i;
            }
            if (cur == k) {
                break;
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] skills = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(findWinningPlayer(skills, k));
    }
}
