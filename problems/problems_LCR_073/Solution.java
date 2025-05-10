package problems.problems_LCR_073;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minEatingSpeed(int[] piles, int h) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] piles = jsonArrayToIntArray(inputJsonValues[0]);
		int h = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minEatingSpeed(piles, h));
    }
}
