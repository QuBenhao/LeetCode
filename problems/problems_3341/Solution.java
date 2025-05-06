package problems.problems_3341;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minTimeToReach(int[][] moveTime) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] moveTime = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(minTimeToReach(moveTime));
    }
}
