package problems.problems_2555;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maximizeWin(int[] prizePositions, int k) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] prizePositions = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maximizeWin(prizePositions, k));
    }
}
