package problems.problems_2545;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[][] sortTheStudents(int[][] score, int k) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] score = jsonArrayToInt2DArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(sortTheStudents(score, k));
    }
}
