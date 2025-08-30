package problems.problems_1051;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int heightChecker(int[] heights) {
        int[] expected = heights.clone();
        Arrays.sort(expected);
        int moves = 0;
        for (int i = 0; i < heights.length; i++) {
            if (heights[i] != expected[i]) {
                moves++;
            }
        }
        return moves;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] heights = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(heightChecker(heights));
    }
}
