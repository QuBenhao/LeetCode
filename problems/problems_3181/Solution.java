package problems.problems_3181;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxTotalReward(int[] rewardValues) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] rewardValues = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxTotalReward(rewardValues));
    }
}
