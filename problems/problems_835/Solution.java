package problems.problems_835;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int largestOverlap(int[][] img1, int[][] img2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] img1 = jsonArrayToInt2DArray(inputJsonValues[0]);
		int[][] img2 = jsonArrayToInt2DArray(inputJsonValues[1]);
        return JSON.toJSON(largestOverlap(img1, img2));
    }
}
