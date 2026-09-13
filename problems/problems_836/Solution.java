package problems.problems_836;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isRectangleOverlap(int[] rec1, int[] rec2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] rec1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] rec2 = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(isRectangleOverlap(rec1, rec2));
    }
}
