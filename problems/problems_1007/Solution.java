package problems.problems_1007;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minDominoRotations(int[] tops, int[] bottoms) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] tops = jsonArrayToIntArray(inputJsonValues[0]);
		int[] bottoms = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(minDominoRotations(tops, bottoms));
    }
}
