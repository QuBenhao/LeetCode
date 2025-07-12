package problems.problems_2410;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int matchPlayersAndTrainers(int[] players, int[] trainers) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] players = jsonArrayToIntArray(inputJsonValues[0]);
		int[] trainers = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(matchPlayersAndTrainers(players, trainers));
    }
}
