package problems.problems_417;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] heights = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(pacificAtlantic(heights));
    }
}
