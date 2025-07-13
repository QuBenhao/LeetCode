package problems.problems_2410;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        Arrays.sort(players);
        Arrays.sort(trainers);
        int i = 0, m = players.length;
        int ans = 0;
        for (int train: trainers) {
            if (players[i] <= train) {
                ++ans;
                if (++i == m) {
                    return m;
                }
            }
        }
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] players = jsonArrayToIntArray(inputJsonValues[0]);
		int[] trainers = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(matchPlayersAndTrainers(players, trainers));
    }
}
