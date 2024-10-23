package problems.problems_3175;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findWinningPlayer(int[] skills, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] skills = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(findWinningPlayer(skills, k));
    }
}
