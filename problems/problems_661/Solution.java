package problems.problems_661;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[][] imageSmoother(int[][] img) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] img = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(imageSmoother(img));
    }
}
