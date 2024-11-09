package problems.problems_LCR_039;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int largestRectangleArea(int[] heights) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] heights = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(largestRectangleArea(heights));
    }
}
