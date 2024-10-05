package problems.problems_LCR_110;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] graph = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(allPathsSourceTarget(graph));
    }
}
