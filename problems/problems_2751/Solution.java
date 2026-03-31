package problems.problems_2751;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<Integer> survivedRobotsHealths(int[] positions, int[] healths, String directions) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] positions = jsonArrayToIntArray(inputJsonValues[0]);
		int[] healths = jsonArrayToIntArray(inputJsonValues[1]);
		String directions = jsonStringToString(inputJsonValues[2]);
        return JSON.toJSON(survivedRobotsHealths(positions, healths, directions));
    }
}
