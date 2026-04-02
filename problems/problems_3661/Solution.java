package problems.problems_3661;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxWalls(int[] robots, int[] distance, int[] walls) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] robots = jsonArrayToIntArray(inputJsonValues[0]);
		int[] distance = jsonArrayToIntArray(inputJsonValues[1]);
		int[] walls = jsonArrayToIntArray(inputJsonValues[2]);
        return JSON.toJSON(maxWalls(robots, distance, walls));
    }
}
