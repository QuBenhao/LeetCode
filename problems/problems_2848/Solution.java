package problems.problems_2848;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfPoints(List<List<Integer>> nums) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<List<Integer>> nums = jsonArrayTo2DIntList(inputJsonValues[0]);
        return JSON.toJSON(numberOfPoints(nums));
    }
}
