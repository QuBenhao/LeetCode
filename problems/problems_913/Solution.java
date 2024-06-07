package problems.problems_913;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int catMouseGame(int[][] graph) {

    }

    @Override
    public Object solve(String[] values) {
        int[][] graph = jsonArrayToInt2DArray(values[0]);
        return JSON.toJSON(catMouseGame(graph));
    }
}
