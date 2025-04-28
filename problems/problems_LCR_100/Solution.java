package problems.problems_LCR_100;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minimumTotal(List<List<Integer>> triangle) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<List<Integer>> triangle = jsonArrayTo2DIntList(inputJsonValues[0]);
        return JSON.toJSON(minimumTotal(triangle));
    }
}
