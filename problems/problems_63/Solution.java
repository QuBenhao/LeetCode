package problems.problems_63;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] obstacleGrid = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(uniquePathsWithObstacles(obstacleGrid));
    }
}
