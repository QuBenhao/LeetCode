package problems.problems_LCR_116;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int findCircleNum(int[][] isConnected) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] isConnected = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(findCircleNum(isConnected));
    }
}
