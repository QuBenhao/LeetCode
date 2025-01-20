package problems.problems_2218;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int maxValueOfCoins(List<List<Integer>> piles, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<List<Integer>> piles = jsonArrayTo2DIntList(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(maxValueOfCoins(piles, k));
    }
}
