package problems.problems_407;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int trapRainWater(int[][] heightMap) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] heightMap = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(trapRainWater(heightMap));
    }
}
