package problems.problems_2140;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long mostPoints(int[][] questions) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] questions = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(mostPoints(questions));
    }
}
