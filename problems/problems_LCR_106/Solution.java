package problems.problems_LCR_106;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isBipartite(int[][] graph) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[][] graph = jsonArrayToInt2DArray(inputJsonValues[0]);
        return JSON.toJSON(isBipartite(graph));
    }
}
