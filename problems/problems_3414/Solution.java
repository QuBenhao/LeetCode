package problems.problems_3414;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] maximumWeight(List<List<Integer>> intervals) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<List<Integer>> intervals = jsonArrayTo2DIntList(inputJsonValues[0]);
        return JSON.toJSON(maximumWeight(intervals));
    }
}
