package problems.problems_Interview_08__02;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<Integer>> pathWithObstacles(int[][] obstacleGrid) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] obstacleGrid = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(pathWithObstacles(obstacleGrid));
    }
}
