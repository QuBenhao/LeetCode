package problems.problems_200;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numIslands(char[][] grid) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[][] grid = jsonArrayToChar2DArray(inputJsonValues[0]);
        return JSON.toJSON(numIslands(grid));
    }
}
