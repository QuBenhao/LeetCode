package problems.problems_2374;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int edgeScore(int[] edges) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] edges = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(edgeScore(edges));
    }
}
